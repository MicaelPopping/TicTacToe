class Client:

    def __init__(self, id, client, addr):

        self.id = id
        self.client = client
        self.addr = addr

    def __str__(self):
        return str(self.id)