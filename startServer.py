#! /bin/ipython3

import socketserver
from threading import Thread
from Game import game
from PlayerSocket import PlayerSocket

"""
1./ Initialiser le jeu
2./ Initialiser le serveur multithread
3./ Démarer le thread game
4./ Démarer le serveur
"""

#Création du Jeu
game = Game()

#Récupération du PNJ
pnj = game.joueurs['PNJ']

#Création de 1000 spheres PNJ de taille 1
for i in range(10000):
    pnj.spheres.append(Sphere(posX= random.randint(1, game.gameSize),posY= random.randint(1,game.gameSize),taille=1))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()
