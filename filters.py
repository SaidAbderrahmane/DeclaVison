import ffmpeg
import os
import shutil
from tkinter import filedialog,Tk
from PIL import Image, ImageFilter
import numpy as np
from skimage.metrics import structural_similarity as ssim


def video_to_images(FPS=0.75):
    """

    :param FPS: correspond au nombre de frame extraite par secondes
    :return: met fin à la fonction
    """
    root = Tk()
    root.withdraw()



    # ouvre une fenêtre pour que l'utilisateur choisisse un fichier (filepath = chemin du fichier choisi)
    filepath = filedialog.askopenfilename(title="Ouvrir un fichier video", filetypes=(("Fichiers vidéo", "*.mov *.mp4"), ("tous les fichiers","*.*")))



    # Dossier de destination pour les images extraites
    if os.path.exists("./image_sortie"):
        shutil.rmtree("./image_sortie")

    # crée le dossier dans le repertoire courant
    Dossier_sortie = "./image_sortie"
    os.makedirs(Dossier_sortie, exist_ok=True)

    # Définir le chemin et le modèle de sortie pour les images
    chemin_sortie = os.path.join(Dossier_sortie, 'frame_%04d.jpg')

    # Utiliser ffmpeg pour extraire les images à raison d'une par seconde
    ffmpeg.input(filepath, ss=0).filter('fps', fps=FPS).output(chemin_sortie).run()


# filtre flou
#----------------------------------------------------------------

def est_floue(image_path, seuil):# quantifie le floue d'une image
    """

    :param image_path: chemin de la photo à quantifier
    :param seuil: seuil pour le filtre floue
    :return:
    """
    # Charger l'image et la convertir en niveaux de gris
    image = Image.open(image_path).convert('L')

    # Appliquer un filtre Laplacien
    laplacian = image.filter(ImageFilter.FIND_EDGES)

    # Convertir l'image filtrée en tableau NumPy
    laplacian_array = np.array(laplacian)

    # Calculer la variance des valeurs Laplaciennes
    variance_laplacian = laplacian_array.var()

    # Vérifier si l'image est floue
    if variance_laplacian < seuil:
        return True, variance_laplacian  # L'image est floue
    else:
        return False, variance_laplacian  # L'image n'est pas floue

def filtre_flou(S=30):
    """

    :param S: seuil du filtre flou
    :return: met fin à la fonction
    """
    chemin_image = "./image_sortie/frame_000"
    c = 1
    while True :
        if c == 10:
            chemin_image = "./image_sortie/frame_00"
        elif c == 100:
            chemin_image = "./image_sortie/frame_0"
        if os.path.exists(chemin_image+str(c)+".jpg"): # vérifie si le fichier existe
            floue, valeur = est_floue(chemin_image + str(c) + ".jpg", seuil=S)
        else:
            C_fin = c # permet de connaitre le numéro de la dernieres image
            break # si le fichier n'existe pas mais fin à la boucle
        if floue:
            os.remove(chemin_image + str(c) + ".jpg") # supprime image flou
        c+=1
    return C_fin
#----------------------------------------------------------------




#filtres doublons
#----------------------------------------------------------------


def filtre_doublons(C_fin,S2=0.96):
    """

    :param C_fin: numéro du fichier de la dernière image de la video après le filtre flou
    :param S2: seuil du filtre doublons
    :return: met fin à la fonction
    """
    chemin_image = "./image_sortie/frame_000"
    chemin_image_2 = "./image_sortie/frame_000"

    c = 1
    c2 = 2
    while True:
        if not(os.path.exists(chemin_image + str(c) + ".jpg")):
            c+=1
            c2+=1
        else:
            break


    while True :
        if c2 >= 10 and c2 < 100:
            chemin_image_2 = "./image_sortie/frame_00"
        elif c2 >= 100:
            chemin_image_2 = "./image_sortie/frame_0"
        if c >= 10 and c < 100:
            chemin_image = "./image_sortie/frame_00"
        elif c >= 100:
            chemin_image = "./image_sortie/frame_0"

        if os.path.exists(chemin_image_2+str(c2)+".jpg") and os.path.exists(chemin_image+str(c)+".jpg"):
            image = Image.open(chemin_image + str(c) + ".jpg").convert('L')
            image_2 = Image.open(chemin_image_2 + str(c2) + ".jpg").convert('L')

            image = np.array(image)
            image_2 = np.array(image_2) # on transforme les images en des tableaux numpy (la fonction ssim ne prend que des tableau numpy en tant qu'arguments)
            score = ssim(image, image_2) # la fct ssim(x,y) quantifie la ressemblance entre la tableau numpy x et y
            if score > S2: # si plus de 96% de ressemblance on suprime l'image en double
                os.remove(chemin_image_2 + str(c2) + ".jpg")
                c2 +=1
            else:
                c = c2
                c2 += 1
        elif not(os.path.exists(chemin_image_2+str(c2)+".jpg")): #si l'image à comparé à déjà était supprimer par le filtre flou, on regarde l'image d'apres (numéro du fichier +1)
            c2 +=1
            pass
        elif not(os.path.exists(chemin_image+str(c)+".jpg")):#si l'image à comparé à déjà était supprimer par le filtre flou, on regarde l'image d'apres (numéro du fichier +1)
            c +=1
            pass
        if c2 >= C_fin or c >= C_fin: # Si le c2 est supérieur au numéro du dernier fichier on met fin au filtres doublon
            break

    return
#----------------------------------------------------------------

def operation(FPS,S,S2): # transforme la video en image et applique les filtres
    """
    :param FPS: correspond au nombre de frame extraite par secondes
    :param S: seuil du filtre flou
    :param S2: seuil du filtre doublons
    :return: met fin à la fonction
    """
    video_to_images(FPS)
    C_fin = filtre_flou(S)
    filtre_doublons(C_fin,S2)
    return

operation(0.75,30,0.96) # démarre l'opération