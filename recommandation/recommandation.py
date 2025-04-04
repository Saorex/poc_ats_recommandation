import pandas as pd
from rake_nltk import Rake
from nltk.corpus import stopwords
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

SYNONYM_GROUPS = [
    {"irriguer", "irrigation", "arrosage", "arroser"},
    {"cultiver", "culture", "plantation", "planter"},
    {"sol", "terre", "terroir"},
    {"fertilisation", "engrais", "nutriment"},
    {"anthracnose", "maladie fongique"},
    {"champignon", "mycose", "pathogène"}
]

def get_synonyms(word):
    """Retourne tous les synonymes associés à un mot"""
    for group in SYNONYM_GROUPS:
        if word in group:
            return group
    return {word}

def charger_donnees():
    """
    Charge les données depuis un fichier Excel, effectue un nettoyage des données et prépare
    la colonne de texte combinée entre le titre et la description de la pratique agricole.
    
    Retourne:
        pd.DataFrame : Un DataFrame pandas nettoyé, avec une colonne 'Texte' combinant 
                       le 'Titre de la pratique' ,la 'Description' et le type de 'Culture'.
    """
    df = pd.read_excel("data/Pratiques_Agricoles DEC 1.xlsx", sheet_name="Les Pratiques Agricoles")
    
    df['Culture'] = df['Culture'].ffill()
    
    df = df.dropna(subset=['Titre de la pratique'])
    
    df['Texte'] = df['Culture'] + ' ' + df['Titre de la pratique'] + ' ' + df['Description'].fillna('')
    
    return df.reset_index(drop=True)

def configurer_rake():
    """
    Configure et retourne une instance de l'algorithme RAKE (Rapid Automatic Keyword Extraction)
    avec des paramètres et des mots vides (stopwords) personnalisés pour le domaine agricole.
    
    Retourne:
        Rake : Instance configurée de l'algorithme RAKE.
    """
    nltk.data.load("tokenizers/punkt/french.pickle")
    
    custom_stopwords = stopwords.words('french') + ['année', 'période', 'saison', 'rendement']
    
    return Rake(
        stopwords=custom_stopwords,
        min_length=1,
        max_length=3,
        include_repeated_phrases=False
    )

def extraire_mots_cles(df):
    """
    Extrait les mots-clés les plus pertinents pour chaque pratique agricole dans le DataFrame.
    
    Paramètres:
        df (pd.DataFrame) : DataFrame contenant les pratiques agricoles.
        
    Retourne:
        pd.DataFrame : Un DataFrame contenant les mots-clés extraits pour chaque pratique.
    """
    rake = configurer_rake()
    
    keywords = []
    
    for idx, row in df.iterrows():
        texte = str(row['Texte']).lower()
        rake.extract_keywords_from_text(texte)
        mots_cles = rake.get_ranked_phrases()[:8]
        
        keywords.append({
            'ID_video': idx,
            'Culture': row['Culture'],
            'Titre': row['Titre de la pratique'],
            'Mots_cles': mots_cles
        })
    
    return pd.DataFrame(keywords)

def trouver_videos(question, keywords_df):
    """
    Recherche les vidéos les plus pertinentes en fonction d'une question et des mots-clés extraits.
    
    Paramètres:
        question (str) : La question de l'utilisateur pour laquelle rechercher des vidéos.
        keywords_df (pd.DataFrame) : DataFrame contenant les mots-clés extraits des pratiques agricoles.
        
    Retourne:
        list : Une liste triée de résultats contenant les vidéos les plus pertinentes.
    """
    rake = configurer_rake()
    rake.extract_keywords_from_text(question.lower())
    question_keywords = rake.get_ranked_phrases()[:5]
    
    resultats = []
    
    for _, video in keywords_df.iterrows():
        score = 0
        mots_communs = set()
        
        for q_kw in question_keywords:
            q_synonyms = set()
            for word in q_kw.split():
                q_synonyms.update(get_synonyms(word))
            
            for v_kw in video['Mots_cles']:
                if any(synonym in v_kw.split() for synonym in q_synonyms):
                    score += 1
                    mots_communs.update(synonym for synonym in q_synonyms if synonym in v_kw.split())
                    break
        
        if score > 0:
            resultats.append({
                'ID_video': video['ID_video'],
                'Culture': video['Culture'],
                'Titre': video['Titre'],
                'Score': score,
                'Mots_cles_communs': list(mots_communs)
            })
    
    return sorted(resultats, key=lambda x: x['Score'], reverse=True)[:3]

'''donnees = charger_donnees()

keywords_df = extraire_mots_cles(donnees)

while(1):

    question = input("Quelle est votre recherche ? \n")

    resultats = trouver_videos(question, keywords_df)

    print(f"Résultats pour : '{question}'\n")
    for res in resultats:
        print(f"[VIDÉO {res['ID_video']}] {res['Titre']}")
        print(f"Culture: {res['Culture']} | Score: {res['Score']}")
        print(f"Mots-clés: {', '.join(res['Mots_cles_communs'])}\n")'''
