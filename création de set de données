import ffmpeg
import os
import shutil
from tkinter import filedialog,Tk

root = Tk()
root.withdraw()

def redimensionner_video(chemin_entré, chemin_sortie, resolution):

    # Définitions des dimensions pour chaque résolution
    qualité = {
        "480p": (854, 480),  # Dimensions approximatives pour 16:9
        "720p": (1280, 720),
        "1080p": (1920, 1080)
    }

    if resolution not in qualité:
        raise ValueError(f"Résolution non supportée : {resolution}. Choisissez parmi {list(qualité.keys())}")

    width, height = qualité[resolution]

    try:
        # Commande FFmpeg pour redimensionner la vidéo
        ffmpeg.input(chemin_entré).filter('scale', width, height).output(chemin_sortie).run()
        print(f"Vidéo redimensionnée avec succès en {resolution} : {chemin_sortie}")
    except Exception as e:
        print(f"Erreur lors du redimensionnement de la vidéo : {e}")

# ouvre une fenêtre pour que l'utilisateur choisisse un fichier (filepath = chemin du fichier choisi)
filepath = filedialog.askopenfilename(title="Ouvrir un fichier video", filetypes=(("Fichiers vidéo", "*.mov *.mp4"), ("tous les fichiers","*.*")))
print(filepath)

input_video = filepath


# Dossier de destination pour les images extraites
if os.path.exists("./image_sortie"):
    shutil.rmtree("./image_sortie")

video_quality = []

for i in ["480p","720p","1080p"]:
    output_video = "./video_redimensionnee_"+i+".MOV"
    video_quality.append(output_video)
    redimensionner_video(input_video, output_video, i)

quality = ["./480p_","./720p_","./1080_"]
fps = ["0.2","1","5"]

for i in range(3):
    for j in range(3):
        Dossier_sortie = quality[i]+fps[j]+"s"
        os.makedirs(Dossier_sortie, exist_ok=True) # crée le dossier dans le repertoire courant

        # Définir le chemin et le modèle de sortie pour les images
        chemin_sortie = os.path.join(Dossier_sortie, 'frame_%04d.jpg')

        # Utiliser ffmpeg pour extraire les images à raison d'une par seconde
        ffmpeg.input(video_quality[i], ss=0).filter('fps', fps=1/float(fps[j])).output(chemin_sortie).run()


