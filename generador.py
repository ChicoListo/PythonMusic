from mingus.containers import Note, Bar
from mingus.midi import midi_file_out
import random

def generar_melodia(num_notas=16):
    notas = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    duraciones = [1, 2, 4, 8]  # entera, media, negra, corchea
    compas = Bar()
    total_duracion = 0

    while total_duracion < 1:  # Asegurarse de llenar un compás completo
        nota = random.choice(notas)
        duracion = random.choice(duraciones)
        nota_duracion = 1 / duracion

        if total_duracion + nota_duracion > 1:
            continue  # Saltar si la nota excede el compás

        compas.place_notes(Note(nota), duracion)
        total_duracion += nota_duracion

    return compas

melodia = generar_melodia()
midi_file_out.write_Bar("melodia.midi", melodia)
