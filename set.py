# Liste de sets
infos = [
    
    {"Toyota","Corolla"}, {"Nissan", "Altima"}, {"Toyota", "Tacoma"}
    
    ]

#Réponse donnée par l'utilisateur
question_01 = input("Quelle marque: ")

#Pour chaque set dans la liste "infos"
for set in infos:

    # Si la réponse de l'utilisateur est présente dans un des Set de la liste "infos"
    if question_01 in set:

        # Imprime le/les Set.s où la réponse est présente
        print(set)
        


