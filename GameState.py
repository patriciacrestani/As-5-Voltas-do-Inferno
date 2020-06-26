class GameState(object):

    ABERTURA = 1
    JOGANDO = 2
    GAME_OVER = 3
    RESTART = 4
    VITORIA = 5

    def __init__(self, state=ABERTURA):
        self.state = state

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state
