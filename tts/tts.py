from gtts import gTTS
from pydub import AudioSegment
import os

def text_to_speech(text, output_file):
    # Génération du fichier audio en MP3 avec gTTS
    tts = gTTS(text=text, lang='fr')
    mp3_file = "temp.mp3"
    tts.save(mp3_file)

    # Conversion du MP3 en OGG
    sound = AudioSegment.from_mp3(mp3_file)
    sound.export(output_file, format="ogg")

    # Suppression du fichier temporaire
    os.remove(mp3_file)

    print(f"Fichier audio généré : {output_file}")
