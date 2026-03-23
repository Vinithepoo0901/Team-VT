txt = open("Toyota_Corolla.txt", "r") #r pour lecture
liste_voiture = txt.readlines() #lire tout et vient creer une liste et chaque ligne de la liste est un element

infos = [] #Liste vide

#Pour chaque ligne dans le .txt
for ligne in liste_voiture:

    #strip pour enlever les espaces au debut et a la fin
    ligne = ligne.strip()

    #split pour creer des elements
    detail = ligne.split(", ")

    #transforme les elements de la liste de chaque ligne en set
    voiture_set = {
        detail[0], detail[1], detail[2], detail[3]
    }

    #on ajoute le set dans la liste infos
    infos.append(voiture_set)

#ferme le fichier
txt.close()

#Réponse donnée par l'utilisateur
question_01 = input("Quelle marque: ")
question_02 = input("Quelle transmission: ")

#Variable pour empecher que le message d<erreur print plusieurs fois dans le for loop.
option_existe = False

#Pour chaque set dans la liste "infos"
for voiture_set in infos:

    # Si la réponse de l'utilisateur est présente dans un des Set de la liste "infos"
    if question_01 in voiture_set and question_02 in voiture_set:

        option_existe = True

        # Imprime le/les Set.s où la réponse est présente
        print(voiture_set)

if option_existe == False: 
    print("Nous n'avons aucune voiture qui correspond à l'entièreté de vos critères. Désolé.")
