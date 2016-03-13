#! /bin/ipython3

import socketserver
import threading
from Game import *
from PlayerSocket import *
"""
1./ Initialiser le jeu
2./ Initialiser le serveur multithread
3./ Démarer le thread game
4./ Démarer le serveur
"""

if __name__ == "__main__":
    HOST, PORT = "localhost", 4444

    server = ThreadedTCPGameServer((HOST, PORT),ThreadedTCPRequestHandler)

    ip, port = server.server_address

    print("Ip: "+str(ip)+", Port: "+str(port))

    server_thread = threading.Thread(target=server.serve_forever)

    server_thread.start()

    print("Server loop running in thread:", server_thread.name)
