#! /bin/ipython3

import random

gameSize=10000

class Game:
    """
    Classe qui définit le jeu

    atributs :
        gameSize : taille du plateau (carré)
        joueurs : Un dictionaire des joueurs avec Nom:joueur
                        (Il y a un joueur nommé PNJ qui contient des spheres qui apparaissent aléatoirement)
    """
    def __init__(self):
        self.gameSize = gameSize
        self.joueurs = dict()
        self.joueurs["PNJ"] = Player(ia="",username="PNJ")


class Player:
    """
    Classe qui définit un joueurs

    atributs :
        ia : l'intéligence atrificiel en cours d'utilisation
        spheres : la liste des spheres du joueurs
        username : le nom d'utilisateur du joueur
    """
    def __init__(self,ia,username):
        self.username = username
        self.spheres = []
        self.ia = ia
        if username != "PNJ":
            self.spheres.append(
                Sphere(
                    posX= random.randint(1, gameSize),
                    posY= random.randint(1, gameSize),
                    taille=10
            ))

class Sphere:
    """
    Classe qui définit une Sphere

    atributs :
        posX : position en X
        posY : position en Y
        taille : taille de la sphere
        coefitionVitesse : coefitien de vitesse a multiplier avec la vitesse max (en fonction de la taille) pour obtenir la vitesse
        angle : angle vers ou se dirrige la sphere(en degres)
    """
    def __init__(self,posX,posY,taille = 1,):
        self.taille = taille;
        self.coefitionVitesse = 0;
        self.angle=0;
        self.posX = posX
        self.posY = posY
