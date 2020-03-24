from server.model.board import Board

board = Board()

class Game:

    gameOver = False
    mines = 9
    flags = 9

    def __init__(self):
        self.gameOver = False