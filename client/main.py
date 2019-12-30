from client import Client

    # Values used to connect to server
TARGET_HOST = 'localhost'
TARGET_PORT = 8888

client = Client(TARGET_HOST, TARGET_PORT)
client.start()