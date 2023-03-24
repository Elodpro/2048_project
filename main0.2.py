#Projet du jeu "2048"
#Auteur : Elod Arifi
#Date de commencement : 01.02.2023
import tkinter
import random
from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox
import copy


#Création fenêtre au millieu de l'écran
width = 500
height = 500
luck2 = 0.80
nmove = 0
score = 0
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
numbers = [[0, 0, 0, 512],
           [1024, 1024, 16, 0],
           [512, 512, 512, 512],
           [0, 2048, 2048, 0]]

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

#Crée le score initiale qui évoluera au fur et a mesure du jeu grâce aux modif dans tass 4. lien modif dans tasse 4 ->(1)
score_label = Label(window, text="0", fg="white", bg="#F4CD58", font="Arial, 10")

#Crée un texte qui dis qu'on a perdu
loose_label = Label(window, text="Vous avez perdu", fg="black", bg="#FCF0CC", font="Arial, 20")

#Création label
width1 = 98 #espacement horizontal en pixels des étiquettes (remarque la taille des labels est en caractères)
height1 = 61 #espacement vertical en pixels des étiquettes

for line in range(len(numbers)):
    for colon in range(len(numbers[line])):
        # construction de chaque label sans le placer
        labels[line][colon] = Label(text=numbers[line][colon], width=8, height=2, borderwidth=2, relief="solid",font=("Comic Sans MS", 14), bg=colors[numbers[line][colon]])

        # placement du label dans la fenêtre par ses coordonnées en pixels
        labels[line][colon].place(x=51 + width1 * colon, y=150 + height1 * line)



#Fonction permettant le tassemant des tuiles
def tasse_4(a,b,c,d):
    global nmove
    global score #(1)
    nmove = 0  # sert à savoir si on a réussi à bouger
    # ici le code va manipuler a,b,c et d

    #Supprimer les 0 ou plutôt déplacer les chiffres vulgairement
    if c == 0 and d > 0:
        c, d = d, 0
        nmove += 1
    if b == 0 and c > 0:
        b,c,d = c,d,0
        nmove += 1
    if a == 0 and b > 0:
        a,b,c,d = b,c,d,0
        nmove += 1

    #Stack les chiffres entre eux ou additionner plutôt
    if a == b and b > 0:
        a,b,c,d = a+b,c,d,0
        score = score + a
        score_label.config(text=score) #(1)

    if b == c and c >0:
        b,c,d = b+c,d,0
        score = score + b
        score_label.config(text=score) #(1)

    if c == d and d >0:
        c,d = c+d,0
        score = score + c
        score_label.config(text=score) #(1)


    # ici on retourne les cinq valeurs en un tableau
    temp=[a,b,c,d] #tableau temporaire de finsw
    return temp



def display():
    print(numbers)
    for line in range(len(numbers)):
        for colon in range(len(numbers[line])):

            if numbers[line][colon] == 0:
                labels[line][colon].config(text="", bg="#E9DBAE")

            else:
                # construction de chaque label sans le placer
                labels[line][colon].config(text=numbers[line][colon], bg=colors[numbers[line][colon]])



def nameGame_change():
    for line in range(len(numbers)):
        for colon in range(len(numbers[line])):
            if numbers[line][colon] ==4096:
                print("4096exe")
                nameGame.config(text="4096")
                display()

#Fonction qui randomise le placement de 2 chiffre de 2 ou 4 sur le tableau
#Aidé par Carlos pour la fonction ci-dessous
def rand_om():
    randomNumbers = random.randint(0, 3)
    randomNumbers2 = random.randint(0, 3)

    while numbers[randomNumbers][randomNumbers2] != 0:
          randomNumbers = random.randint(0, 3)
          randomNumbers2 = random.randint(0, 3)

          if numbers[randomNumbers][randomNumbers2] == 0:

              if random.random() < luck2:
                numbers[randomNumbers][randomNumbers2] = 2

              else:
                  numbers[randomNumbers][randomNumbers2] = 4
              break
    else:

        if random.random() < luck2:
            numbers[randomNumbers][randomNumbers2] = 2

        else:
            numbers[randomNumbers][randomNumbers2] = 4
    display()


#Recommemce la partie en supprimant toute les tuiles avant que la fonctions random s'éxecute
def new_game():
    global score
    global numbers

    numbers = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    score = 0
    score_label.config(text="0")
    nameGame.config(text="2048")
    fin_label.destroy()
    btn_restart_end.destroy()
    loose_label.destroy()
    rand_om()
    rand_om()
    display()

#Boutton "Nouveau"
btn_newGame = Button(window, text="Nouveau", width=7, borderwidth=3, height=1, relief="raised", bg="#F1C232", font=("Comic Sans MS", 11),command=new_game)


#Texte lorsque le joueur à atteint 8192
fin_label = Label(window, text="Fin de la partie", fg="black", bg="#FCF0CC", font="Arial, 20")


#Permet de supprimer le texte de fin de jeu une fois avoir appuyer sur le bouton "Encore ?"
def supp_end_txt():
    global score
    global numbers

    numbers = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    score = 0
    score_label.config(text="0")
    nameGame.config(text="2048")
    fin_label.destroy()
    btn_restart_end.destroy()
    rand_om()
    rand_om()
    display()


#Boutton restart le jeu après avoir gagné
btn_restart_end = Button(window, text="Encore ?", width=10, borderwidth=3, height=1,
relief="raised",bg="#F1C232", font=("Comic Sans MS", 11), command=supp_end_txt)


#Fonction permettant de gèrer les messages de la tuile 2048 1x et afficher la fin de partie en ayant obtenu 8192
msg_2048 = 1
def win():
    global msg_2048
    global fin_label
    global btn_restart_end
    for line in range(len(numbers)):
        for colon in range(len(numbers[line])):
            #Permet de changer le jeu en ayant obtenu 8192
            if numbers[line][colon] == 8192:
                fin_label.place(x=40, y=400)
                btn_restart_end.place(x=40, y=440)
                print("Win")
                #Permet d'afficher un message qu'une seul fois lorsqu'on atteint 2048
            if msg_2048 == 1:
                if numbers[line][colon] == 2048:
                    messagebox.showinfo("Félicitation", "Vous avez obtenu 2048")
                    msg_2048 = 0


#perdu
def loose():
    global numbers
    moveperdu = 0
#copied my numbers
    numbers2 = copy.deepcopy(numbers)
    #move left
    for ligne in range(4):
        [numbers2[ligne][0], numbers2[ligne][1], numbers2[ligne][2], numbers2[ligne][3]] = tasse_4(numbers2[ligne][0],numbers2[ligne][1],numbers2[ligne][2],numbers2[ligne][3])
        moveperdu += nmove
    #move right
    for ligne in range(4):
        [numbers2[ligne][3], numbers2[ligne][2], numbers2[ligne][1], numbers2[ligne][0]] = tasse_4(numbers2[ligne][3],numbers2[ligne][2],numbers2[ligne][1],numbers2[ligne][0])
        moveperdu += nmove
    #move up
    for line in range(4):
        [numbers2[0][line], numbers2[1][line], numbers2[2][line], numbers2[3][line]] = tasse_4(numbers2[0][line],numbers2[1][line],numbers2[2][line],numbers2[3][line])
        moveperdu += nmove
    #move down
    for line in range(4):
        [numbers2[3][line], numbers2[2][line], numbers2[1][line], numbers2[0][line]] = tasse_4(numbers2[3][line],numbers2[2][line],numbers2[1][line],numbers2[0][line])
        moveperdu += nmove
    if moveperdu == 0:
        messagebox.showinfo("PERDU","Vous avez perdu !")
        

#Fonction lorsqu'il n'y a plus la possibilité de bouger met un message
#Qu'on a perdu
#def loose():



def nameGame_change():
    for line in range(len(numbers)):
        for colon in range(len(numbers[line])):

            if numbers[line][colon] ==4096:
                print("4096exe")
                nameGame.config(text="4096")

            if numbers[line][colon] == 8192:
                print("8192exe")
                nameGame.config(text="8192")

                display()

#Fonction lorsqu'il n'y a plus la possibilité de bouger met un message
#Qu'on a perdu


#Déplacer les chiffres à gauche
def move_left(event):
    global nmove
    tempnmove = 0

    for ligne in range(len(numbers)):
        [numbers[ligne][0], numbers[ligne][1], numbers[ligne][2], numbers[ligne][3]]= tasse_4(numbers[ligne][0],
        numbers[ligne][1],numbers[ligne][2],numbers[ligne][3])
        tempnmove += nmove
        nameGame_change()
    if tempnmove == 0:
        print("ok")
    else:
        win()
        rand_om()
        loose()
    display()


#Déplacer les chiffres à droite
def move_right(event):
    global nmove
    tempnmove = 0

    for ligne in range(len(numbers)):
        [numbers[ligne][3], numbers[ligne][2], numbers[ligne][1], numbers[ligne][0]] = tasse_4(numbers[ligne][3],
        numbers[ligne][2],numbers[ligne][1],numbers[ligne][0])
        tempnmove += nmove
        nameGame_change()
    if tempnmove == 0:
        print("Move")
    else:
        win()
        rand_om()
        loose()
    display()


#Déplacer les chiffres en haut
def move_top(event):
    global nmove
    tempnmove = 0

    for ligne in range(len(numbers)):
        [numbers[0][ligne], numbers[1][ligne], numbers[2][ligne], numbers[3][ligne]] = tasse_4(numbers[0][ligne],
        numbers[1][ligne],numbers[2][ligne],numbers[3][ligne])
        tempnmove += nmove
        nameGame_change()
    if tempnmove == 0:
       print("Move")
    else:
        win()
        rand_om()
        loose()
    display()


#Déplacer les chiffres en bas
def move_bottom(event):
    global nmove
    tempnmove = 0

    for ligne in range(len(numbers)):
        [numbers[3][ligne], numbers[2][ligne], numbers[1][ligne], numbers[0][ligne]] = tasse_4(numbers[3][ligne],
        numbers[2][ligne],numbers[1][ligne],numbers[0][ligne])
        tempnmove += nmove
        nameGame_change()
    if tempnmove == 0:
        print("Move")
    else:
        win()
        rand_om()
        loose()
    display()




#Attribuer les touches au déplacement
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("w",move_top)
window.bind("s",move_bottom)


#Afficher les choses crée
background_label.place(x=40, y=138)
ScoreSq.place(x=35, y=20)
ScoreTxt.place(x=40, y=22)
rulesTxt.place(x=35, y=80)
nameGame.place(x=345, y=16)
btn_newGame.place(x=380, y=76)
score_label.place(x=42, y=47)
display()
window.mainloop()
