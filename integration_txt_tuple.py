"""

Projet_02: Fichier d'extraction de .txt
Nom: Tommy Brunelle, Vincent Goulet

"""
try:

    txt = open("caracteistiques.txt", "r") 
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

except FileNotFoundError:
    print("Erreur : Le fichier .txt désiré est introuvable.\
        \nAssurez-vous qu'il n'y ait pas d'erreurs dans son nom et qu'il soit bien\
        \ndans le même dossier que votre main.py\n")

except IndexError:
    print("Erreur : Votre .txt ne contient pas le bon nombre d'éléments.\
        \nAssurez-vous d'avoir 3 éléments (2 virgules) dans votre fichier.")
    exit()