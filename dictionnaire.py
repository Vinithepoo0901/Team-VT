#Liste de dictionnaires
infos = [
    {"marque": "Toyota", "modele": "Corolla"},
    {"marque": "Nissan", "modele": "Altima"},
    {"marque": "Toyota", "modele": "Tacoma"}
]

#Réponse donnée par l'utilisateur
question_01 = input("Quelle marque: ")

#Pour chaque dictionnaire dans la liste "infos"
for dictionnaire in infos:

    #Si la réponse de l'utilisateur est présente dans un dictionnaire dans la liste "infos"
    if question_01 == dictionnaire["marque"]:

        #Imprime le/les dictionnaire.s où la réponse est présente.
        print(dictionnaire)
        