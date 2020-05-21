class ClientsList:

    def __init__(self):
        self.list = dict([])


    def insert(self, client):
        self.list[client.id] = client


    def getClient(self, id):
        return self.clients[id]

    def __str__(self):

        result = '{'
        for k, v in self.list.items():
            result += '[' + str(k) + ', ' + str(v) + ']' 
        result += '}'

        return result
