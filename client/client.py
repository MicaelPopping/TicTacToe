import socket


class Client:

    def __init__(self, target_host, target_port):
        self.TARGET_HOST = target_host
        self.TARGET_PORT = target_port
        self.current_state = 1
        self.client = None


        # [ 1] - Start the connection.
        # [ 2] - Initial state of application.
        # [ 3] - .
        # [ 0] - Terminate the connection.
        # [-1] - Shut down the state machine.
    def start(self):
            # Client state machine.
        while True:
                # Connection State.
            if self.current_state == 1:
                self.current_state = self.connection_state()
                # Connected State.
            if self.current_state == 2:
                self.current_state = self.connected_state()


        # State(1): Connecting whit the server.
         # Client sends -> ("/connect") (/connected) <- / Goes to the beginning of the game.
    def connection_state(self):
            # Initiating the connection to the server.
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.TARGET_HOST, self.TARGET_PORT))
            # Awaiting server response.
        message = self.client.recv(1024)
        message = message.decode()
            # Checking server response.
        if message == '/connected':
            return 2
        else:
            return -1

        # State(2): Application start.
         # Client sends -> (/play) (/queue) <- / Goes to the queue.
         # Client sends -> (/quit) (/unplugged) <- / Goes to the queue.
    def connected_state(self):
        return