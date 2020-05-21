from threading import Thread
from client import Client

class news_clients(Thread):

    def __init__(self, server, clients):
        Thread.__init__(self)
        self.server = server
        self.clients = clients

    def run(self):

        current_id = 0
            # Loop looking for new clients.
        while True:
                # Finding and adding a new client to the client list.
            new_client, new_addr = self.server.accept()
            self.clients.insert(Client(current_id, new_client, new_addr))
                # Start listening client.
            # ...
                # Answers the client that he is connected.
            new_client.send(b'/connected')
                # Increment the current client id.
            current_id += 1

                # test code.
            print('Connected client.')
            #print(self.clients)
