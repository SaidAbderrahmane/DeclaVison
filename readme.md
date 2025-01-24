# Projet Détection d'Incidents

Ce projet utilise le modèle YOLO pour la détection d'incidents à partir de vidéos. Il inclut des étapes de prétraitement, d'entraînement et d'évaluation des modèles sur deux types d'incidents : incidents automobiles et incidents domestiques.

## Structure du Projet

- **`data`** : Contient les données brutes pour le cas d'utilisation (petites vidéos d'incidents).
- **`models`** : Contient les modèles préentraînés pour le traitement d'images (YOLOv8l et YOLOv8n).
- **`notebooks`** : Contient les notebooks  de développement et de test.
- **`docs`** : Contient les supports et documents relatifs au projet.
- **`preprocess.py`** : Contient le code pour l'échantillonnage des images à partir des vidéos.
- **`train.py`** : Contient le code pour l'entraînement des modèles YOLO.
- **`evaluate.py`** : Contient le code pour l'évaluation du modèle sur des vidéos afin de détecter les incidents.
- **`dataset_incident_auto`** : Dataset généré avec Roboflow, incluant les labels et les données divisées pour l'entraînement sur les incidents automobiles.
- **`dataset_incident_maison`** : Dataset généré avec Roboflow, incluant les labels et les données divisées pour l'entraînement sur les incidents domestiques.

## Fonctionnalités Principales

1. **Prétraitement des Vidéos**
   - Extraction d'images à partir de vidéos pour générer des datasets utilisables.
   - Script : `preprocess.py`.

2. **Entraînement des Modèles**
   - Utilisation de YOLOv8 pour entraîner les modèles sur des datasets personnalisés.
   - Supporte deux datasets distincts : incidents automobiles et incidents domestiques.
   - Script : `train.py`.

3. **Évaluation des Modèles**
   - Test des modèles entraînés sur des vidéos pour détecter et identifier les incidents.
   - modifier le scripts en speciefiant quel model à lancer
   - Script : `evaluate.py`.

## Prérequis

- Python 3.8 ou ultérieur.
- Bibliothèques nécessaires (à installer avec pip) :
  ```bash
  pip install -r requirements.txt
  ```
- CUDA (optionnel) pour accélérer l'entraînement si un GPU est disponible.

## How to run

- Placer les videos sur le dossier `Data` pour faire le prétraitement dessus
- Télécharger les 2 datasets éttiquetés et annotés (labeled) depuis les liens suivant:
 https://drive.google.com/file/d/1El_sRUwU0cmG6Uiqu3iHwVYcO14c5acH/view?usp=sharing
 https://drive.google.com/file/d/1swy9Y3EuvsqM5IZB4XpC87ELBCOEe59b/view?usp=sharing


## Datasets

- **`dataset_incident_auto`** : Utilisé pour les incidents automobiles.
- **`dataset_incident_maison`** : Utilisé pour les incidents domestiques.
- Les datasets incluent les labels et les images, générés avec Roboflow.


