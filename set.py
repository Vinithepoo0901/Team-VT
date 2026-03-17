infos = [
    
    {"Toyota","Corolla"}, {"Nissan", "Altima"}
    
    ]

question_01 = input("Quelle marque: ")


for set in infos:
    if question_01 in set:
        print(set)
        break


