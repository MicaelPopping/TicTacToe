from server import Server  
 
    # Server informations.
HOST = 'localhost'
PORT = 8888

server = Server(HOST, PORT)
server.start()