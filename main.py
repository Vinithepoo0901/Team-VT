"""

Projet_02: Filtreur de voiture
Nom: Tommy Brunelle, Vincent Goulet

"""
import tkinter as tk
import integration_csv_dictionnaire as le_csv
import integration_txt_tuple as le_txt

# La liste vide qui sert à stocker nos choix finaux sélectionnés à partir du tkinter.
choix_finaux = []

# Les variables qui contiennent une liste créée avec les éléments présents dans "Marque" pour chaque dictionnaire dans lecsv.infos
# set efface les doublons présents
marque = {dictionnaire["Marque"] for dictionnaire in le_csv.infos}
type = {dictionnaire["Type"] for dictionnaire in le_csv.infos}
consomation = {dictionnaire["Consomation"] for dictionnaire in le_csv.infos}
prix = {dictionnaire["Prix"] for dictionnaire in le_csv.infos}
transmission = {tuple[1] for tuple in le_txt.infos_supplementaire}
traction = {tuple[2] for tuple in le_txt.infos_supplementaire}

# Variable qui contient la liste de dictionnaires utilisés pour générer les titres et les choix de notre tkinter.
questions = [
    {"question": "Quelle Marque ?", "options": marque},
    {"question": "Quel type ?", "options": type},
    {"question": "Quel consommation ?", "options": consomation},
    {"question": "Quel est votre budget ?", "options": prix},
    {"question": "Quelle transmission?", "options": transmission},
    {"question": "Quelle traction?", "options": traction}
]

# Variable à insérer dans nos fonctions qui permet de générer tous les menus tkinter nécessaires.
question_actuelle = 0

def montrer_question_actuelle():

    """
    Entrées: Les strings établis pour les titres/questions et les éléments dans la liste "options".
    Sortie: Les choix sélectionnés sur chaque menu tkinter.
    But: Permettre de générer une boite textuelle avec questions et options à choisir.

    """

    global question_actuelle

    # Effacer le contenu du menu tkinter affiché avant de générer le prochain.
    for widget in root.winfo_children():
        widget.destroy()

    # Générer le titre du menu tkinter.
    tk.Label(
        root,
        text = questions[question_actuelle]["question"],
        font = ("Arial", 12, "bold")
    ).pack(pady = 12) 

    # Générer les choix dans le menu tkinter.
    for element in questions[question_actuelle]["options"]:
        tk.Button(
            root,
            text = element,
            width = 20,
            #
            command = lambda choix = element: choisir_option(choix)
        ).pack(pady = 6)


def choisir_option(choix_selectionner):

    """
    Entrées: Les choix sélectionnés sur chaque menu tkinter de la fonction précédente.
    Sortie: Un fichier .txt
    But: Permettre au client de voir quel véhicule correspond à ses critères et si nous l'avons en stock.

    """

    global question_actuelle

    # Ajouter le choix sélectionné à la fin de la liste choix_finaux.
    choix_finaux.append(choix_selectionner)

    # Changer la valeur de la variable globale question_actuelle pour générer la prochaine question.
    question_actuelle += 1

    # Si la valeur de question_actuelle < 5, on relance la fonction montrer_question_actuelle
    if question_actuelle < len(questions):
        montrer_question_actuelle()

    else:
        resultat = open("resultat.txt", "w")

        # Variable pour éviter de write "Aucune de nos voitures ne correspond à vos critères" pour chaque véhicule qui ne correspond pas.
        voiture_compatible = False

        for dictionnaire in le_csv.infos:
            if (
                dictionnaire["Marque"] == choix_finaux[0] and
                dictionnaire["Type"] == choix_finaux[1] and
                dictionnaire["Consomation"] == choix_finaux[2] and
                dictionnaire["Prix"] == choix_finaux[3]):
                
                for texte in le_txt.infos_supplementaire:
                    if (
                        texte[0] == dictionnaire["Modele"] and
                        texte[1] == choix_finaux[4] and
                        texte[2] == choix_finaux[5]):

                        resultat.write("Voitures qui correspondent a vos criteres: \n")
                        resultat.write("-" + dictionnaire["Modele"])

                        voiture_compatible = True

        if voiture_compatible == False:
            resultat.write("Aucune de nos voitures ne correspond a vos criteres.")

        resultat.close()

        # Fermer la fenêtre tkinter.
        root.destroy() 

# Créer/lancer notre fenêtre tkinter.
root = tk.Tk()
montrer_question_actuelle()

#Permet d'utiliser tkinter et faire que command= soit fonctionnel.
root.mainloop()