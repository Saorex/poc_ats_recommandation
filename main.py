import whisper
import torch
import time
import sounddevice as sd
import numpy as np
import wave

# Paramètres d'enregistrement
SAMPLE_RATE = 16000  # Taux d'échantillonnage
DURATION = 5  # Durée d'enregistrement en secondes
OUTPUT_FILE = "live_audio.wav"

def record_audio(filename, duration, sample_rate):
    print("Enregistrement en cours...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
    sd.wait()  # Attendre la fin de l'enregistrement
    print("Enregistrement terminé.")

    # Sauvegarde au format WAV
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 16-bit PCM
        wf.setframerate(sample_rate)
        wf.writeframes(audio.tobytes())

# Charger le modèle Whisper
print("Chargement du modèle...")
model = whisper.load_model("small")

# Capture de l'audio
record_audio(OUTPUT_FILE, DURATION, SAMPLE_RATE)

# Transcription avec mesure du temps
start_time = time.time()
result = model.transcribe(OUTPUT_FILE)
end_time = time.time()

# Affichage des résultats
print("Texte transcrit:", result["text"])
print(f"Temps de réponse: {end_time - start_time:.2f} secondes")