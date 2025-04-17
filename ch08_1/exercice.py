#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import os
import json
from copy import deepcopy

# TODO: Définissez vos fonction ici
def exercice1_(fichier1, fichier2):
    with open(fichier1, 'r', encoding='utf-8') as f1, open(fichier2, 'r', encoding='utf-8') as f2:
        texte1=f1.read()
        texte2=f2.read()
        texte1=texte1.lower()
        texte2=texte2.lower()
        words1= texte1.strip().split()
        words2= texte2.strip().split()
        i=-1
        for ch1 in  words1:
            i+=1
            if not(ch1== words2[i]):
                print(f"il y a un probleme dans le mot : {words1[i]}")
            else:
                pass
    f1.close()
    f2.close()
def exercice2_(fichier_texte):
    with open(file_path1, encoding="utf-8") as f1, open(file_path2, "w", encoding="utf-8") as f2:
        f2.write(f1.read().replace(" ", "   "))
        return f2
def exercice3_(notes.txt, fichier2):
    with open(notes.text, 'r', encoding='utf-8') as f1, open(fichier2, 'r', encoding='utf-8') as f2:
        texte1=f1.readline()
        for n, count in texte1.items():
            if n== "%":
                f2.write(count[n:n+5])
    with open(seuils.json, 'r', encoding='utf-8') as file:
        f= json.load(file)
                        
        
                
"""Écrire un programme qui compare le contenu de deux fichiers et signale la première différence rencontrée.

Écrire un programme qui recopie un fichier texte en triplant tous les espaces entre les mots. (vous pouvez ouvrir deux fichiers avec l’instruction with).

Écrire un programme qui lit chaque ligne d’un fichier notes.txt (chaque ligne contient une note en pourcentage) et qui réécrit, 
dans un nouveau fichier, les notes avec, à côté, les mentions « A », « B », etc. en fonction d’un dictionnaire de correspondance fourni dans le fichier seuils.json.

Reprenez l’exercice du livre de recettes (recettes.py) et créez une base de données dans un fichier qui permet d’ajouter, modifier, supprimer des recettes. Vous êtes libre de choisir le type de format de fichier. Essayez d'en supporter plusieurs, par exemple en détectant l'extension du fichier de recettes passé à la fonction.

Écrire un programme qui lit un fichier texte exemple.txt et retourne une liste de tous les nombres présents dans le fichier, en ordre croissant.

Écrire un programme qui lit un fichier et qui recopie une ligne sur deux dans un autre fichier."""
if __name__ == '__main__':
    if not os.path.exists("output"):
        os.mkdir("output")

    # TODO: Appelez vos fonctions ici, mettez vos fichiers de sortie dans le dossier "output".

