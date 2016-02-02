#! /bin/ipython3

import matplotlib.pyplot as plt
import numpy
import string
import json
from Game import *

game = Game()

for i in range(3):
    name = ''.join(random.choice("sdfsdfgsd") for i in range(5))
    game.joueurs[name]= Player("",name)

pnj = game.joueurs['PNJ']

for i in range(1000):
    pnj.spheres.append(Sphere(posX= random.randint(1, 10000),posY= random.randint(1, 10000),taille=1))

for joueur in game.joueurs.values():
    for sphere in joueur.spheres:
        plt.scatter(sphere.posX,sphere.posY, marker='o', c=numpy.random.rand(3,1), s=sphere.taille)

plt.show()

#print(json.dumps(game, default=lambda o: o.__dict__))
