csv = open("caracteristiques.csv", "r")
liste_voiture = csv.readlines()

# La liste vide qui sert à stocker nos dictionnaires finaux créés à partir du .csv.
infos = [] 

for ligne in liste_voiture:

    ligne = ligne.strip()
    detail = ligne.split(";")

    # La variable qui vient placer chaque detail de notre .split à une catégorie dans un dictionnaire.
    dictionnaire = {
        "Modele": detail[0],
        "Marque": detail[1],
        "Type": detail[2],
        "Consomation" : detail[3],
        "Prix" : detail[4]
        }

    # Ajouter le dictionnaire créé à la fin de la liste infos.
    infos.append(dictionnaire)

csv.close()


