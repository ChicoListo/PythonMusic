import numpy as np
from pydub import AudioSegment
from pydub.playback import play

def generar_onda_sinusoidal(frecuencia, duracion, volumen=0.5, sample_rate=44100):
    t = np.linspace(0, duracion, int(sample_rate * duracion), False)
    onda = 0.5 * np.sin(2 * np.pi * frecuencia * t)  # Corrección: falta un asterisco (*) entre np.pi y frecuencia
    
    # Convertir a un segmento de audio
    audio = (onda * (2**15 - 1) * volumen).astype(np.int16)
    return AudioSegment(audio.tobytes(), frame_rate=sample_rate, sample_width=2, channels=1)

# Generar una nota sinusoidal de 440 Hz (nota A) durante 2 segundos
onda_sinusoidal = generar_onda_sinusoidal(440, 2)

# Reproducir la onda generada
play(onda_sinusoidal)


