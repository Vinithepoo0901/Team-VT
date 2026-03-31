csv = open("Projet-2-excel.csv", "r") #r pour lecture
liste_voiture = csv.readlines() #lire tout et vient creer une liste et chaque ligne de la liste est un element

infos = [] #Liste vide

#Pour chaque ligne dans le .txt
for ligne in liste_voiture:

    #strip pour enlever les espaces au debut et a la fin
    ligne = ligne.strip()

    #split pour creer des elements
    detail = ligne.split(";")

    #transforme les elements de la liste de chaque ligne en dictionnaire
    dictionnaire = {
        "Marque": detail[0],
        "Type": detail[1],
        "Consomation" : detail[2],
        "Prix de depart" : detail[3]
    }

    #on ajoute le set dans la liste infos
    infos.append(dictionnaire)

#ferme le fichier
csv.close()

print (detail[0])

