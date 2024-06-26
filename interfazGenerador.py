import tkinter as tk
from mingus.containers import Note
from mingus.midi import fluidsynth

# Inicializar Fluidsynth
fluidsynth.init("ruta_a_tu_sf2.sf2")

def reproducir_nota(nota):
    fluidsynth.play_Note(Note(nota))

root = tk.Tk()
root.title("Compositor de Música")

# Crear botones para notas
notas = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
for nota in notas:
    button = tk.Button(root, text=nota, command=lambda n=nota: reproducir_nota(n))
    button.pack(side=tk.LEFT)

root.mainloop()

