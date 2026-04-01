import tkinter as tk
import integration_csv_dictionnaire as lecsv
import integration_txt_set_01 as txt

choix = [] #Liste vide qui va devenir notre liste d'options choisies final.

marque = list(set(dictionnaire["Marque"] for dictionnaire in lecsv.infos))
type = list(set(dictionnaire["Type"] for dictionnaire in lecsv.infos))
consomation = list(set(dictionnaire["Consomation"] for dictionnaire in lecsv.infos))
prix = list(set(dictionnaire["Prix de depart"] for dictionnaire in lecsv.infos))
transmission = list(set(i[0] for i in txt.infos_01))
traction = list(set(i[1] for i in txt.infos_01))

#Liste de nos questions (Va falloir trouver le moyen de changer ca par dequoi qui va chercher nos valeurs direct dans le .csv et .txt)
questions = [
    {"question": "Quelle Marque ?", "options": marque},
    {"question": "Quel type ?", "options": type},
    {"question": "Quel consommation ?", "options": consomation},
    {"question": "Quel est votre budget ?", "options": prix},
    {"question": "Quelle transmission?", "options": transmission},
    {"question": "Quelle traction?", "options": traction}
]

# Nous permet d'aller chercher le dictionnaire qu'on veut dans la liste questions pour nos fonctions.
question_actuelle = 0

def montrer_question_actuelle():
    #On apporte la valeur globale de question_actuelle dans la fonction au-lieu d<en creer une.
    global question_actuelle

    # Effacer la fenêtre juste avant de construire la prochaine. (Merci google)
    for widget in root.winfo_children():
        widget.destroy()

    # Pour le titre/question de chaque box
    tk.Label(
        root,
        text=questions[question_actuelle]["question"],
        font=("Arial", 12, "bold")
    ).pack(pady=12) #.pack ajoute le tk.label dans la fenetre ouverte et pady est juste l'espace vertical ajoutee en haut et en bas du texte

    # Pour afficher les options dans la box
    for i in questions[question_actuelle]["options"]:
        tk.Button(
            root,
            text=i,
            width=20,
            command=lambda choix=i: choisir_option(choix)
            #command=lambda permet de faire qqchose juste quand un bouton est cliqué
            #Donc quand on clique sur ce que l'on veut, command= lance la fonction choisir_option
        ).pack(pady=6)


def choisir_option(choix_selectionner):
    global question_actuelle

    choix.append(choix_selectionner) #On vient ajouter le choix cliqué dans notre liste finale "choix"

    question_actuelle += 1 #On change la valeur de la variable globale question_actuelle

    # Si valeur question_actuelle < longueur de mon nombre d<elements dans la liste "questions" (len = 3)
    if question_actuelle < len(questions):
        # Relancer la fonction montrer_question_actuelle
        montrer_question_actuelle()
    else: # Si question_actuelle == len(questions)
        resultat = open("resultat.txt", "w")

        voiture_compatible = False #Pour ne pas write "aucun match 70000000 fois"

        for i in lecsv.infos:
            if (
            i["Marque"] == choix[0] and
            i["Type"] == choix[1] and
            i["Consomation"] == choix[2] and
            i["Prix de depart"] == choix[3]):
                resultat.write("Voitures qui correspondent a vos criteres: ")
                resultat.write(i["Modele"])

                voiture_compatible = True

        if voiture_compatible == False:
            resultat.write("Aucun match dsl")

        resultat.close()
        
        root.destroy() #ferme notre menu de bouton tkinter

# Creer/lancer notre fenetre tkinter
root = tk.Tk()

#Creer tout ce qu<il y a dans notre fenetre tkinter
montrer_question_actuelle()
root.mainloop() #Permet de runner tkinter et de pouvoir cliquer sur les options et faire que command= soit fonctionnel.