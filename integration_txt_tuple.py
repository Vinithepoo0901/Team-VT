"""

Projet_02: Fichier d'extraction de .txt
Nom: Tommy Brunelle, Vincent Goulet

"""
txt = open("caracteristiques.txt", "r") 
liste_voiture = txt.readlines()

# La liste vide qui sert à stocker nos tuples finaux créés à partir du .txt.
infos_supplementaire = [] 

for ligne in liste_voiture:

    ligne = ligne.strip()
    detail = ligne.split(", ")

    # La variable qui vient placer chaque detail de notre .split dans un tuple.
    voiture_tuple = (detail[0], detail[1], detail[2]) 

    # Ajouter le tuple créé à la fin de la liste infos_supplementaire.
    infos_supplementaire.append(voiture_tuple)

txt.close()

