from threading import Thread

class news_clients(Thread):

    def __init__(self, server):
        Thread.__init__(self)
        self.server = server

    def run(self):

        current_client_id = 0
            # Loop looking for new clients.
        while True:
                # Awaiting new client.
            new_client, new_addr = self.server.accept()
                #
                # ...
                # Answers the client that he is connected.
                # ...
            print('Connected client.')
                # Increment the current client id.
            current_client_id += 1
