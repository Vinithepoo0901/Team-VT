infos = [
    {"marque": "Toyota", "modele": "Corolla"},
    {"marque": "Nissan", "modele": "Altima"}
]

question_01 = input("Quelle marque: ")

for voiture in infos:
    if question_01 == voiture["marque"]:
        print(voiture)
        break