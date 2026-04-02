txt = open("Toyota_Corolla.txt", "r") #r pour lecture
liste_voiture = txt.readlines() #lire tout et vient creer une liste et chaque ligne de la liste est un element

infos_01 = [] #Liste vide

#Pour chaque ligne dans le .txt
for ligne in liste_voiture:

    #strip pour enlever les espaces au debut et a la fin
    ligne = ligne.strip()

    #split pour creer des elements
    detail = ligne.split(", ")

    #transforme les elements de la liste de chaque ligne en tuple
    voiture_tuple = (detail[0], detail[1]) 

    #on ajoute le tuple dans la liste infos
    infos_01.append(voiture_tuple)

#ferme le fichier
txt.close()

