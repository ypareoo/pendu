#Augeix Adrien

# code source et tout les fichiers disponibles sur mon github
# https://github.com/tokageki/pendu


"""

  888888                        8888888b.                8888888b.                        888
    "88b                        888  "Y88b               888   Y88b                       888
     888                        888    888               888    888                       888
     888  .d88b.  888  888      888    888 888  888      888   d88P .d88b.  88888b.   .d88888 888  888
     888 d8P  Y8b 888  888      888    888 888  888      8888888P" d8P  Y8b 888 "88b d88" 888 888  888
     888 88888888 888  888      888    888 888  888      888       88888888 888  888 888  888 888  888
     88P Y8b.     Y88b 888      888  .d88P Y88b 888      888       Y8b.     888  888 Y88b 888 Y88b 888
     888  "Y8888   "Y88888      8888888P"   "Y88888      888        "Y8888  888  888  "Y88888  "Y88888
   .d88P
 .d88P"
888P"

"""

import sqlite3
import random #pour sortir un nombre au pif
import tkinter #logique
from tkinter import messagebox #pour plus tard




root = tkinter.Tk() #initialise tkinter
root.geometry("640x480") #fait une fenètre de 640x480 pixels
root.resizable(False, False) #bloque la possiblilité de la redimensionner
root.title('Jeu du pendu - AUGEIX Adrien') #mets le titre
root.iconbitmap('game.ico') #met la MAGNIFIQUE icone faite par mes soins

conn = sqlite3.connect('score.db')
c = conn.cursor()

#Création d'un tableau contenant les scores
c.execute("""CREATE TABLE IF NOT EXISTS SCORE (
        name                VARCHAR             NOT NULL,
        score               INTEGER             NOT NULL
        )""")

pseudo = "Enjoliveur"



def genMot(): #prends un mot dans la liste
    global motATrouver
    motATrouver = ""
    with open("liste_de_mots.txt") as f: #ouvre la liste de mots
        lines = f.readlines() #j'ai vraiment besoin de commenter "readlines" ?
        motATrouver = random.choice(lines)[:-1].upper() #prends une ligne aleatoire dans le mot
    return motATrouver


def motTiret():#fait le mot avec les -
    global motJeu
    motJeu = ""
    for i in range(len(motATrouver)): #fait un mot avec des - en fonction de la longeur du mot de base
        motJeu += "-"


def clearScreen(): #efface tout les elements de l'écran
    global message, text, boutonValider, labelImage, texteJeu, messageError, boutonValider, boutonQuitter
    message.destroy()
    labelImage.destroy()
    texteJeu.destroy()
    messageError.destroy()
    text.destroy()
    boutonValider.destroy()
    boutonRelancer.destroy()
    boutonQuitter.destroy()

    genGame() #relance une nouvelle partie


def game(): #fonction qui vérifie si le joueur gagne ou pas et affiche l'avancement du jeu
    global motJeu, motATrouver, nombreTentative, listeLettres, lettreDansLaListe, partieCreee, boutonQuitter
    print(motATrouver)
    texteJeu.config(text=motJeu)
    lettreDansLaListe = False
    pasPerdreVie = False #permet de perdre une vie dans ce tour
    if nombreTentative >= 6 : #si le joueur n'a plus de vie il  a perdu
        texteJeu.config(text="Tu as perdu\n le mot était "+ motATrouver)
        text.destroy() #supprime les elements non nécéssaires et affiche les boutons pour relancer et quitter
        boutonValider.destroy()
        boutonRelancer.pack()
        boutonQuitter.pack()
    elif motJeu == motATrouver :
        c.execute("INSERT INTO SCORE VALUES (?, ?)", ((pseudo),(6-nombreTentative)))
        conn.commit()
        texteJeu.config(text="Tu as gagné ! \n le mot était "+ motATrouver)
        photo.config(file="cake.gif") #affiche le gateau de portal quand on a gagné (hehe)
        text.destroy() #supprime les elements non nécéssaires et affiche les boutons pour relancer et quitter
        boutonValider.destroy()
        boutonRelancer.pack()
        boutonQuitter.pack()

def quitter(): #ferme la fenètre
    global root
    root.destroy()

def genGame(): #génère une nouvelle partie
    global motJeu, motATrouver, nombreTentative, listeLettres, lettreDansLaListe, partieCreee, text, message, boutonValider, texteJeu, messageError,photo,labelImage, boutonRelancer, boutonQuitter
    motJeu = "" #remets les valeurs à zero et les initialise si elles existent pas
    nombreTentative = 0
    listeLettres = "" #besoin de faire une variable vide pour faire des += plus tard
    lettreDansLaListe = False
    pasPerdreVie = False

    text = tkinter.Entry(width = 10) #affiche les elements
    message = tkinter.Label(text="Bienvenue dans le jeu du pendu")
    boutonValider = tkinter.Button(root, text = "valider lettre", command = validerLettre, height=2, width=90)
    texteJeu = tkinter.Label(text="")
    messageError = tkinter.Label(text="")
    photo = tkinter.PhotoImage(file="frame_0.gif")
    labelImage = tkinter.Label(image=photo)
    boutonRelancer = tkinter.Button(root, text = "Relancer une partie", command = clearScreen, height=2, width=90)
    boutonQuitter = tkinter.Button(root, text = "Quitter", command = quitter, height=2, width=90)
    labelImage.image = photo

    message.pack() #pack tout
    text.pack()
    boutonValider.pack()
    labelImage.pack()
    texteJeu.pack()
    messageError.pack()
    boutonValider.pack()


    genMot() #prends un mot dans la liste
    motTiret() #transforme le mot en tirets
    game() #lance le jeu




def validerLettre(): #fait fonctionner le bouton valider et lance le jeu
    global lettre, listeLettres, lettreDansLaListe, pasPerdreVie, nombreTentative, motJeu, motATrouver
    pasPerdreVie = False #fonction qui permet de pas perdre de vie :D
    lettre = text.get().upper() #prends la lettre / mot dans la zone de texte
    if lettre != motATrouver:
        if len(lettre) > 1 or lettre == "" or lettre == " ": #si l'utilisateur ne rentre pas de lettre, un espace ou rentre plusieurs lettre il est averti et ne perdsd pas de vie
            pasPerdreVie = True #desactive la perte de vie pour ce tour, la lettre rentrée n'étant pas valide
            messageError.config(text="merci de rentrer une lettre valide")
        else :
            messageError.config(text="") #efface le message d'erreur
    else :
        motJeu = motATrouver
        pasPerdreVie = True
    for i in range(len(listeLettres)):
        if lettre == listeLettres[i]: #verifie si la lettre a déjà été utilisée
            messageError.config(text="lettre déjà utilisée")
            pasPerdreVie = True #si c'est le cas, désactive la perte de vie dans ce tour
            lettreDansLaListe = True #si la lettre est déjà dans la liste "listeLettre", ce bool empèche d'ajouter la lettre dans la liste
    if lettreDansLaListe == False and pasPerdreVie == False: #si la lettre n'est pas déjà dans la liste, ça la met dedans
        listeLettres += lettre
        messageError.config(text="")
    for i in range(len(motATrouver)):
        if lettre == motATrouver[i]: #verifie si la lettre est dans le mot
            pasPerdreVie = True #si la lettre est dans le mot la variable est mise sur true pour dire de pas faire perdre de vie
            motJeu = motJeu[:i] + motATrouver[i] + motJeu[i+1:] #remplace le "-" correspondant à la lettre qui a été trouvée
    if pasPerdreVie == False : #fait perdre une vie
        nombreTentative += 1
        messageError.config(text="vous perdez une vie")
        photo.config(file="frame_" + str(nombreTentative) + ".gif") #affiche l'image du pendu
    game() #continue de faire tourner le jeu, si on utilise des boucles l'interface freeze, noice

c.execute("SELECT * FROM SCORE")
score = c.fetchall()
tableauScore = []

score.sort()

if not score:
    print("Aucun score enregistré.")
else :
    print("meilleur score : " + str(score[len(score)-1][0]) + " avec " + str(score[len(score)-1][1]) + " points !")

genGame() #lance une partie quand le programme est ouvert

root.mainloop()
