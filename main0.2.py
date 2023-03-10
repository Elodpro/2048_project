#Projet du jeu "2048"
#Auteur : Elod Arifi
#Date de commencement : 01.02.2023
import tkinter
import random
from tkinter import *
import tkinter.font as tkFont
from tasse4 import *


#Création fenêtre au millieu de l'écran
width = 500
height = 500
window = Tk()
window.config(bg="#FCF0CC")
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
x = (screenwidth / 2) - (width / 2)
y = (screenheight / 2) - (height / 2)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))
window.resizable(False, False)
window.title("2048")


#Variables
colors = {
    0: "#E9DBAE",
    2: "#FFE599",
    4: "#F5D36C",
    8: "#F1C232",
    16: "#CDA220",
    32: "#BF9000",
    64: "#F6B26B",
    128: "#E69138",
    256: "#B45F06",
    512: "#E06666",
    1024: "#C4CF7E",
    2048: "#A893B2",
    4096: "#91B4C5",
    8192: "#3382A8"
}

#Pré crée les tuilles avec leur chiffre
numbers = [[2, 0, 0, 0],
           [32, 0, 16, 0],
           [0, 8, 0, 2],
           [0, 4, 4, 0]]

#Créer les espaces vides pour les tuilles
labels = [[None, None, None, None],
          [None, None, None, None],
          [None, None, None, None],
          [None, None, None, None]]


#Création du carré de score
ScoreSq = Label(window, width=16, height=3, borderwidth=2, relief="solid", bg="#F4CD58")
ScoreTxt = Label(window, text="score", bg="#F4CD58", font=("Comic Sans MS", 13))

#Texte de la règle de jeu
rulesTxt = Label(window, text="Obtenez le nombre 8192", bg="#FCF0CC", font=("Verdana",14))

#Nom du jeu "2048"
nameGame = Label(window, text="2048", bg="#FCF0CC", font=("Comic Sans MS", 33))

#Fond du jeu
background_label = Label(window, width=58, height=17, relief="solid", borderwidth=3, bg="#F6D97F")

#Création label
width1 = 98 #espacement horizontal en pixels des étiquettes (remarque la taille des labels est en caractères)
height1 = 61 #espacement vertical en pixels des étiquettes

for line in range(len(numbers)):
    for colon in range(len(numbers[line])):
        # construction de chaque label sans le placer
        labels[line][colon] = Label(text=numbers[line][colon], width=8, height=2, borderwidth=2, relief="solid",font=("Comic Sans MS", 14), bg=colors[numbers[line][colon]])

        # placement du label dans la fenêtre par ses coordonnées en pixels
        labels[line][colon].place(x=51 + width1 * colon, y=150 + height1 * line)


def display():
    print(numbers)
    for line in range(len(numbers)):
        for colon in range(len(numbers[line])):

            if numbers[line][colon] == 0:
                labels[line][colon].config(text="", bg="#E9DBAE")

            else:
                # construction de chaque label sans le placer
                labels[line][colon].config(text=numbers[line][colon], bg=colors[numbers[line][colon]])


#Fonction qui randomise le placement de 2 chiffre de 2 sur le tableau
#Aide Carlos pour la fonction ci-dessous
def rand_om():
    randomNumbers = random.randint(0, 3)
    randomNumbers2 = random.randint(0, 3)

    while numbers[randomNumbers][randomNumbers2] != 0:
          randomNumbers = random.randint(0, 3)
          randomNumbers2 = random.randint(0, 3)
          if numbers[randomNumbers][randomNumbers2] == 0:
              numbers[randomNumbers][randomNumbers2] = 2
              break
    else:
        numbers[randomNumbers][randomNumbers2] = 2
    display()


#Recommemce la partie avec 2x2 chiffres aléatoirement placé
def new_game():
    global numbers
    numbers = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    rand_om()
    rand_om()
    display()

#Boutton "Nouveau"
btn_newGame = Button(window, text="Nouveau", width=7, borderwidth=3, height=1, relief="raised", bg="#F1C232", font=("Comic Sans MS", 11),command=new_game)


#Déplacer les chiffres à gauche
def move_left(event):
    for ligne in range(len(numbers)):
        [numbers[ligne][0], numbers[ligne][1], numbers[ligne][2], numbers[ligne][3],n]= tasse_4(numbers[ligne][0],numbers[ligne][1],numbers[ligne][2],numbers[ligne][3])
    rand_om()
    display()


#Déplacer les chiffres à droite
def move_right(event):
    for ligne in range(4):
        [numbers[ligne][3], numbers[ligne][2], numbers[ligne][1], numbers[ligne][0],n] = tasse_4(numbers[ligne][3],
        numbers[ligne][2],numbers[ligne][1],numbers[ligne][0])
    rand_om()
    display()


#Déplacer les chiffres en haut
def move_top(event):
    for ligne in range(4):
        [numbers[0][ligne], numbers[1][ligne], numbers[2][ligne], numbers[3][ligne],n] = tasse_4(numbers[0][ligne],
        numbers[1][ligne],numbers[2][ligne],numbers[3][ligne])
    rand_om()
    display()


#Déplacer les chiffres en bas
def move_bottom(event):
    for ligne in range(4):
        [numbers[3][ligne], numbers[2][ligne], numbers[1][ligne], numbers[0][ligne],n] = tasse_4(numbers[3][ligne],
        numbers[2][ligne],numbers[1][ligne],numbers[0][ligne])
    rand_om()
    display()



#Attribuer les touches au déplacement
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("w",move_top)
window.bind("s",move_bottom)


#Afficher les choses crée
background_label.place(x=40, y=138)
ScoreSq.place(x=35, y=20)
ScoreTxt.place(x=70, y=22)
rulesTxt.place(x=35, y=80)
nameGame.place(x=345, y=16)
btn_newGame.place(x=380, y=76)

display()
window.mainloop()
