"""

Projet_02: Fichier d'extraction de .csv
Nom: Tommy Brunelle, Vincent Goulet

"""
try:

    csv = open("caracteristiques.csv", "r")
    liste_voiture = csv.readlines()

    # La liste vide qui sert à stocker nos dictionnaires finaux créés à partir du .csv.
    infos = [] 

    for ligne in liste_voiture:

        ligne = ligne.strip()
        detail = ligne.split(";")

        # La variable qui vient placer chaque detail de notre .split à une catégorie dans un dictionnaire.
        dictionnaire = {
            "Modele": detail[1],
            "Marque": detail[2],
            "Type": detail[3],
            "Consommation" : detail[4],
            "Prix" : detail[5]
            }

        # Ajouter le dictionnaire créé à la fin de la liste infos.
        infos.append(dictionnaire)

    csv.close()

except FileNotFoundError:
    print("Erreur : Le fichier .csv désiré est introuvable.\
        \nAssurez-vous qu'il n'y ait pas d'erreurs dans son nom et qu'il soit bien\
        \ndans le même dossier que votre main.py\n")