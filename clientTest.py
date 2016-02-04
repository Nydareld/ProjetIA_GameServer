#! /bin/ipython3

import time
import socket

ip = "localhost"
port = 7777

def client(ip, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    message = "mess no:"
    cpt= 1
    while True:
        try:
            sock.sendall(bytes(message+str(cpt), 'ascii'))
            response = str(sock.recv(1024), 'ascii')
            print("Received: {}".format(response))
            cpt+=1
            time.sleep(1)
        finally:
            pass
            #sock.close()


client(ip, port)
