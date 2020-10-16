import random #pour sortir un nombre au pif
import tkinter #logique
from tkinter import messagebox #pour plus tard


root = tkinter.Tk() #initialise tkinter
root.geometry("640x480") #fait une fenètre de 640x480 pixels
root.resizable(False, False) #bloque la possiblilité de la redimensionner 
root.title('Jeu du pendu - AUGEIX Adrien') #mets le titre
root.iconbitmap('game.ico') #met la MAGNIFIQUE icone faite par mes soins




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


motJeu = ""
nombreTentative = 0
jeuEnCours = True
listeLettres = ""
lettreDansLaListe = False
rejouer = True
pasPerdreVie = False



def game(): #fonction qui vérifie si le joueur gagne ou pas et affiche l'avancement du jeu
    global motJeu, motATrouver, jeuEnCours, nombreTentative, listeLettres, lettreDansLaListe, rejouer, partieCreee
    if jeuEnCours:
        texteJeu.config(text=motJeu)
        lettreDansLaListe = False
        pasPerdreVie = False #permet de perdre une vie dans ce tour
        if nombreTentative >= 6 : #si le joueur n'a plus de vie il  a perdu
            texteJeu.config(text="Tu as perdu\n le mot était "+ motATrouver)
            jeuEnCours = False #coupe le jeu
        elif motJeu == motATrouver :
            texteJeu.config(text="Tu as gagné ! \n le mot était "+ motATrouver)
            jeuEnCours = False
            photo.config(file="cake.gif")


def genGame(): #génère une nouvelle partie
    genMot()
    motTiret()
    game()




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
        photo.config(file="frame_" + str(nombreTentative) + ".gif")
    game()


text = tkinter.Entry(width = 10)
message = tkinter.Label(text="Bienvenue dans le jeu du pendu")
boutonValider = tkinter.Button(root, text = "valider lettre", command = validerLettre, height=2, width=90)
texteJeu = tkinter.Label(text="")
messageError = tkinter.Label(text="")
photo = tkinter.PhotoImage(file="frame_0.gif")
labelImage = tkinter.Label(image=photo)
labelImage.image = photo 


message.pack()
text.pack()
boutonValider.pack()
labelImage.pack()
texteJeu.pack()
messageError.pack()
genGame()



root.mainloop()
