#! /bin/ipython3
import math
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
                    random.randint(1, gameSize),
                    random.randint(1, gameSize),
                    taille=150))
            self.spheres.append(
                Sphere(
                    random.randint(1, gameSize),
                    random.randint(1, gameSize),
                    taille=1500))
            self.spheres.append(
                Sphere(
                    random.randint(1, gameSize),
                    random.randint(1, gameSize),
                    taille=2090))
            self.spheres.append(
                Sphere(
                    random.randint(1, gameSize),
                    random.randint(1, gameSize),
                    taille=1320))
            self.spheres.append(
                Sphere(
                    random.randint(1, gameSize),
                    random.randint(1, gameSize),
                    taille=1328))
            self.spheres.append(
                Sphere(
                    random.randint(1, gameSize),
                    random.randint(1, gameSize),
                    taille=2225))
            self.spheres.append(
                Sphere(
                    random.randint(1, gameSize),
                    random.randint(1, gameSize),
                    taille=1211))
            self.spheres.append(
                Sphere(
                    random.randint(1, gameSize),
                    random.randint(1, gameSize),
                    taille=2512))
            self.spheres.append(
                Sphere(
                    random.randint(1, gameSize),
                    random.randint(1, gameSize),
                    taille=1230))
            self.spheres.append(
                Sphere(
                    random.randint(1, gameSize),
                    random.randint(1, gameSize),
                    taille=1000))
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
    def __init__(self,posX,posY, taille = 1):
        self.taille = taille
        self.vectVitesse = [0,0]
        self.vectAcceleration = [0,0]
        self.vectPos = [posX,posY]
        self.t=0

    def getInertie(self):
        return 1/2*taille*vitesse**2

    def posNextTick(self):
        x=self.vectPos[0]+self.vectVitesse[0]+1/2*self.vectAcceleration[0]**2
        y=self.vectPos[1]+self.vectVitesse[1]+1/2*self.vectAcceleration[1]**2

        x+=50*math.cos(self.t)#La ca tourne(pour les tests)
        y+=50*math.sin(self.t)

        #print("x="+str(int(x))+"y="+str(int(y)))
        self.t+=1/30

        if x > gameSize :
            x=gameSize
        if y > gameSize :
            y=gameSize

        if x < 0 :
            x=0
        if y < 0 :
            y=0
        return [int(x),int(y)]

    def vitesseNextTick(self):
        vx=self.vectVitesse[0]+self.vectAcceleration[0]
        vy=self.vectVitesse[1]+self.vectAcceleration[1]
        return [int(vx),int(vy)]

    def normeVitesse(self):
        return math.sqrt(self.vectVitesse[0]**2 + self.vectVitesse[1]**2 )

    def normeVitesseMax(self):
        return ((1/self.taille)*1000)+10

    def rayon(self):
        return math.sqrt(self.taille)/2

    def distanceTo(self,sphere2):
        #print(str(math.sqrt((sphere2.vectPos[0]-self.vectPos[0])**2  + (sphere2.vectPos[1]-self.vectPos[1])**2 )))
        return math.sqrt((sphere2.vectPos[0]-self.vectPos[0])**2  + (sphere2.vectPos[1]-self.vectPos[1])**2 )

    def canJoin(self,sphere2):
        return (
            ( self.distanceTo(sphere2)< self.rayon() ) # la distance entre les 2 centres < la moité du rayon de l'autre
            and                                                           # ET
            (0.8*self.taille > sphere2.taille)                            # la sphere2 fais moins de 80% de la taille de cette sphere ci
            )

    def join(self,sphere2,player2):
        if self.canJoin(sphere2):
            print("On a mangé, D="+str(self.distanceTo(sphere2))+" ,R="+str(self.rayon()))
            self.taille += sphere2.taille
            return [player2,sphere2]
        return None
