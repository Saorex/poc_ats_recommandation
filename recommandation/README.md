# 🌱 Système d'Extraction de Mots-Clés Agricoles

## 📌 Description
Outil intelligent pour :
- Analyser des fiches techniques agricoles
- Identifier les termes clés et leurs synonymes
- Répondre aux questions avec pertinence

--- 

## 🚀 Fonctionnalités Principales
- Nettoyage automatique des données Excel
- Détection de 8 mots-clés par pratique agricole
- Gestion de 6 groupes de synonymes prédéfinis
- Interface de recherche conversationnelle

---

## 📦 Guide d'Installation

1. Télécharger le fichier Excel : [Pratiques_Agricoles DEC 1.xlsx]

2. Installer les dépendances :

    pip install pandas rake-nltk nltk openpyxl

3. Initialiser les ressources linguistiques :

    python -m nltk.downloader punkt stopwords

---

## 🛠️ Structure du Code

Groupes de synonymes (extrait) :

    SYNONYM_GROUPS = [
        {"irriguer", "irrigation", "arrosage"},
        {"cultiver", "culture", "plantation"}
    ]

Fonction de recherche principale :

    def trouver_videos(question, keywords_df):
        # 1. Analyse sémantique de la question
        # 2. Comparaison avec les mots-clés étendus
        # 3. Retourne les 3 meilleurs résultats

---

## 💡 Exemple d'Utilisation

Demande utilisateur :
- Quelle est votre recherche ? 
- Comment améliorer l'arrosage du maïs ?

Sortie générée :

    [VIDÉO 15] Techniques modernes d'irrigation
    Culture: Maïs | Score: 4/5
    Mots-clés associés : irrigation, système goutte-à-goutte

---

## 📊 Performances
- Traitement de 100+ entrées en <500ms
- Précision accrue grâce aux synonymes

---

## 🔧 Personnalisation

Ajouter un groupe de synonymes :

    SYNONYM_GROUPS.append({
        "ravageur", 
        "insecte", 
        "parasite"
    })

Modifier les stopwords :

    custom_stopwords = ["période", "saison"] + stopwords.words('french')

---
