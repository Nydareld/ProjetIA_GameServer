#! /bin/ipython3
import socketserver
import threading

class ThreadedTCPGameServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
        super().__init__(server_address, RequestHandlerClass, bind_and_activate)

        self.cur_thread = threading.current_thread()
        self.playerThreads = []

        print(
            "Server en écoute sur le thread "+
            self.cur_thread.name+
            "\nIp: "+
            str(self.server_address[0])+
            ", Port: "+
            str(self.server_address[1])+
            "\n")

    def process_request(self, request, client_address):
        """Start a new thread to process the request."""
        t = threading.Thread(target = self.process_request_thread,
                             args = (request, client_address))
        t.daemon = self.daemon_threads
        self.playerThreads.append(t)
        t.start()
        print("List des threads Joueurs: \n"+ self.threadListDebug() )

    def threadListDebug(self):
        res = ""
        for th in self.playerThreads:
            res += th.name +"\n"
        return res

class ThreadedTCPRequestHandler(socketserver.StreamRequestHandler):

    def setup(self):
        self.cur_thread = threading.current_thread()
        super().setup()
        print(
            "Client connécté sur le thread "+
            self.cur_thread.name+
            "\nIp: "+
            str(self.client_address[0])+
            ", Port: "+
            str(self.client_address[1])+
            "\n")

    def handle(self):
        
        while True:
            data = str(self.request.recv(1024), 'ascii')
            response = bytes("{}: {}".format(self.cur_thread.name, data), 'ascii')
            self.request.sendall(response)
