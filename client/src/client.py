import socket
from ui import UIInitialApp, UIGameWaiting


class Client:

    def __init__(self, target_host, target_port):
        self.TARGET_HOST = target_host
        self.TARGET_PORT = target_port
        self.current_state = 1
        self.client = None


        # [ 1] - Start the connection. (connection_state())
        # [ 2] - Initial state of application. (initial_app_state())
        # [ 3] - Queue to play. (game_waiting_state)
        # [ 4] - Making the move. (playing_state)
        # [ 5] - Waiting to play. (waiting_state)
        # [ 6] - .
        # [ 0] - Terminate the connection.
        # [-1] - Shut down the state machine.
    def start(self):
            # Client state machine.
        while True:
                # Connection State.
            if self.current_state == 1:
                self.current_state = self.connection_state()
                # Initial App Satate .
            if self.current_state == 2:
                self.current_state = self.initial_app_state()
                # Game Waiting Satate .
            if self.current_state == 3:
                self.current_state = self.game_waiting_state()
            

        # State(1): Connecting whit the server.
         # Client sends -> ("/connect") (/connected) <- / Goes to the beginning of the game.
    def connection_state(self):
            # Initiating the connection to the server.
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.TARGET_HOST, self.TARGET_PORT))
            # Awaiting server response.
        response = self.client.recv(1024).decode()
            # Checking server response.
        if response == '/connected':
            return 2
        else:
            return -1

        # State(2): Application start.
         # Client sends -> (/play) (/queue) <- / Goes to the queue.
         # Client sends -> (/quit) (/disconnected) <- / Goes to the end.
    def initial_app_state(self):
            # Start UI.
        ui = UIInitialApp()
        user_input = ui.start()
            # Handle client choice.
        if user_input == 1:
            self.client.send(b'/play')
        elif user_input == 0:
            self.client.send(b'/quit')
            # Awaiting server response.
        response = self.client.recv(1024).decode()
            # Checking server response.
        if response == '/queue':
            return 3
        elif response == '/disconnected':
            return 0


        # State(3): Queue to play.
         # Client sends -> ('/game'/play) ...
         #                                (/play_it)<- / Goes to the play.
         #                                (/wait)<- / Goes to the play wait.
    def game_waiting_state(self):
            # Start UI.
        ui = UIGameWaiting()
        ui.start()
            # Awaiting server response.
        response = self.client.recv(1024).decode()
            # Checking server response.
        if response == '/play_it':
            return 4
        elif response == '/wait':
            return 5