

from playsound import playsound
import threading
import os

songs = {    
    "bad" : "/BAD BUNNY - SI VEO A TU MAMÁ  YHLQMDLG [Visualizer] - Bad Bunny.mp3"

}


def playMusic(name):
    route = songs.get(name.lower())
    if not route or not os.path.exists(route):
        print("❌ Canción no encontrada o ruta inválida.")
        return
    threading.Thread(target=playsound, args=(route,), daemon=True).start()
    print("Reproduciendo música... 🎵")

def leer_pdf(ruta_pdf):
    print(f"Leyendo PDF: {ruta_pdf}")

def saludar(nombre):
    print(f"Hola, {nombre}! ¿En qué puedo ayudarte hoy?")
