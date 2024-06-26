import librosa 
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Cargar una canción
archivo_audio = 'F:\Música\Zoé - MTV Unplugged Música De Fondo/04 - No Me Destruyas (Live).flac'  # Especifica la ruta de tu archivo de audio
y, sr = librosa.load(archivo_audio)

# Extraer espectrograma
espectrograma = librosa.feature.melspectrogram(y=y, sr=sr)
espectrograma_db = librosa.power_to_db(espectrograma, ref=np.max)

# Visualizar el espectrograma
plt.figure(figsize=(10, 4))
librosa.display.specshow(espectrograma_db, sr=sr, x_axis='time', y_axis='mel')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de Mel')
plt.tight_layout()
plt.show()
