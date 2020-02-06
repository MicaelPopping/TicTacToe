import socket
from news_clients import news_clients

class Server:

    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.server = None

    
    def start(self):
            # Start server.
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.HOST, self.PORT))
        self.server.listen()
            # Start news_clients thread.
        t_news_clients = news_clients(self.server)
        t_news_clients.start()

        print('Server start.')
            # .
        t_news_clients.join()