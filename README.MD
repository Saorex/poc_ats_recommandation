# poc-Recommandation

Ce POC utilise **Whisper** d'OpenAI pour transcrire l'audio en direct.

## Installation

1. **Installer les dépendances** (Ubuntu/Debian) :
   ```bash
   sudo apt update && sudo apt install -y python3 python3-pip portaudio19-dev ffmpeg
   ```
2. **Installer les bibliothèques Python** :
   ```bash
   pip install openai-whisper sounddevice numpy torch torchaudio
   ```

### 🔹 Optionnel : Utiliser un environnement virtuel
Si vous souhaitez isoler les dépendances du projet, utilisez un environnement virtuel :
```bash
python3 -m venv venv
source venv/bin/activate  # Sous Windows : venv\Scripts\activate
pip install --upgrade pip
pip install openai-whisper sounddevice numpy torch torchaudio
```

## 🎧 Utilisation

1. **Lancer l'enregistrement et la transcription** :
   ```bash
   python main.py
   ```
2. **Sortie attendue** :
   ```bash
   Enregistrement terminé.
   Texte transcrit : "Bonjour !"
   Temps de réponse : 2.3s
   ```
