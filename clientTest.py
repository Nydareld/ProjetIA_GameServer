#! /bin/ipython3

import time
import math
import socket
import json
import random

import pygame
from pygame.locals import *

import numpy

WHITE = (255, 255, 255)

ip = "localhost"
port = 4444

pygame.init()
screen = pygame.display.set_mode((500, 500))

screen.fill(WHITE)
pygame.display.flip()

def client(ip, port,screen):

    tick = 0
    erreur = 0

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))

    player=input("Username ?:")
    data = dict()
    data["Username"]=player
    data["Ia"]="rand"

    sock.sendall(bytes(json.dumps(data,default=lambda o: o.__dict__)+"END",'ascii'))

    #response = str(sock.recv(1024), 'ascii')
    #print("{}".format(response))
    #message = "mess no:"
    #cpt= 1
    while True:
        tick +=1
        try:
            #sock.sendall(bytes(message+str(cpt), 'ascii'))
            #data = str(sock.recv(1024), 'ascii')
            #print("{}".format(response))
            #cpt+=1
            #time.sleep(1)
            data = recv_end(sock)
            #print(data)
            try:
                game = json.loads(data)
                affGame(game,screen)
            except json.JSONDecodeError:
                erreur += 1
                print("Erreur Json. Tick ="+str(tick))
                print("Recu :\n"+data)
                print("Ratio Erreur = "+str(erreur/tick))
            #fig.clf()
        finally:
            pass
            #sock.close()

def affGame(game,screen):
    screen.fill([255, 255, 255])
    for joueur in game.values():
        color= (random.randint (0,255),random.randint (0,255),
                            random.randint (0,255))
        for sphere in joueur:
            x=sphere[0][0]
            y=sphere[0][1]
            s=sphere[1]
            pygame.draw.circle(screen, color, [int(x/20),int(y/20)], int(math.sqrt(s)/2))
    pygame.display.flip()


def recv_end(the_socket):
    End='END'
    total_data=[];data=''
    while True:
            data=str(the_socket.recv(8192),'ascii')
            if End in data:
                total_data.append(data[:data.find(End)])
                break
            total_data.append(data)
            if len(total_data)>1:
                #check if end_of_data was split
                last_pair=total_data[-2]+total_data[-1]
                if End in last_pair:
                    total_data[-2]=last_pair[:last_pair.find(End)]
                    total_data.pop()
                    break
    return ''.join(total_data)

client(ip, port,screen)
