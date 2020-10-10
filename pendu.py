import random

def dessinPendu(nb): #array qui contient les images
    tab=[
    """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """
        ,
    """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      | |
       |
    ==============
    """
    ]
    return tab[nb]



with open("liste_de_mots.txt") as f: #ouvre la liste de mots
    lines = f.readlines() 
    motATrouver = random.choice(lines)[:-1].upper() #prends une ligne aleatoire dans le mot 
print(motATrouver)

motJeu = ""
nombreTentative = 0
jeuEnCours = True
listeLettres = ""
lettreDansLaListe = False

for i in range(len(motATrouver)): #fait le mot avec les -
    motJeu += "-"



while jeuEnCours:
    print(motJeu) #affiche le mot en cours de recherche 

    lettreDansLaListe = False
    pasPerdreVie = False #permet de perdre une vie dans ce tour
    if nombreTentative >= 6 : #si le joueur n'a plus de vie il  a perdu
        print("Tu as perdu")
        jeuEnCours = False #coupe le jeu
        break

    lettre = input("entrez la lettre : ").upper() 

    if len(lettre) > 1 or lettre == "" or lettre == " ": #si l'utilisateur ne rentre pas de lettre, un espace ou rentre plusieurs lettre il est averti et ne perdsd pas de vie
        print(f"merci de rentrer une lettre correcte")
        pasPerdreVie = True #desactive la perte de vie pour ce tour, la lettre rentrée n'étant pas valide

    for i in range(len(listeLettres)):
        if lettre == listeLettres[i]: #verifie si la lettre a déjà été utilisée
            print(listeLettres[i])
            print("lettre déjà utilisée")
            pasPerdreVie = True #si c'est le cas, désactive la perte de vie dans ce tour
            lettreDansLaListe = True #si la lettre est déjà dans la liste "listeLettre", ce bool empèche d'ajouter la lettre dans la liste
    if lettreDansLaListe == False and pasPerdreVie == False: #si la lettre n'est pas déjà dans la liste, ça la met dedans
        listeLettres += lettre

    for i in range(len(motATrouver)):
        if lettre == motATrouver[i]: #verifie si la lettre est dans le mot
            
            pasPerdreVie = True #si la lettre est dans le mot la variable est mise sur true pour dire de pas faire perdre de vie
            motJeu = motJeu[:i] + motATrouver[i] + motJeu[i+1:] #remplace le "-" correspondant à la lettre qui a été trouvée
    if pasPerdreVie == False : #fait perdre une vie
        nombreTentative += 1
        print(dessinPendu(nombreTentative))

    if motJeu == motATrouver :
        print(motATrouver)
        print("BRAVO ! TU AS GAGNE !") #je crois que c'est assez explicite
        break
        
