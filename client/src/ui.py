import os


class UI:

    def __init__(self):
        pass


    def clean(self):
        if os.name == 'posix':
            os.system('clear')
        elif os.system == 'nt':
            os.system('cls')


    def header(self):
        self.clean()
        print('\t-=-= TicTacToe =-=-\n')


class UIInitialApp(UI):

    def __init__(self):
        UI.__init__(self)


    def start(self):

        while True:
            self.header()
            print('1. Procurar partida.')
            print('0. Sair.\n')
            user_input = input('Insira sua opção: ')

            if self.validate_input(user_input):
                return int(user_input)
    

    def validate_input(self, input):
        if input == '1' or input == '0':
            return True
        return False


class UIGameWaiting(UI):

    def __init__(self):
        UI.__init__(self)


    def start2(self):
        self.header()
        print('Procurando por partida, aguarde...')