import pygame
import time

# Inicializar Pygame
pygame.mixer.init()

# Cargar archivo de sonido
archivo_sonido = 'F:\Música\Kidd Keo - The Giant/01 - Lollypop.mp3'  # Proveer la ruta correcta a tu archivo de sonido
sound = pygame.mixer.Sound(archivo_sonido)

# Reproducir sonido
sound.play()

# Esperar a que el sonido termine de reproducirse
time.sleep(sound.get_length())

# Cerrar Pygame
pygame.mixer.quit()