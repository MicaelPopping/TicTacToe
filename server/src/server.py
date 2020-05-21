import socket
from news_clients import news_clients
from clients_list import ClientsList

class Server:

    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port

    
    def start(self):
            # Start server.
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.HOST, self.PORT))
        server.listen()
            # Start clients list.
        clients = ClientsList()
            # Start news_clients thread.
        t_news_clients = news_clients(server, clients)
        t_news_clients.start()

        print('Server start.')
            # .
        t_news_clients.join()