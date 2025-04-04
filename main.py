from speak_to_text.speak_to_text import transcrire_audio
from recommandation.recommandation import charger_donnees, extraire_mots_cles, trouver_videos

def main():
    print("Chargement des données...")
    donnees = charger_donnees()
    keywords_df = extraire_mots_cles(donnees)

    print("Veuillez poser une question après l'enregistrement.")
    question = transcrire_audio()

    print(f"Résultats pour : '{question}'")
    resultats = trouver_videos(question, keywords_df)

    for res in resultats:
        print(f"[VIDÉO {res['ID_video']}] {res['Titre']}")
        print(f"Culture: {res['Culture']} | Score: {res['Score']}")
        print(f"Mots-clés: {', '.join(res['Mots_cles_communs'])}\n")

if __name__ == "__main__":
    main()
