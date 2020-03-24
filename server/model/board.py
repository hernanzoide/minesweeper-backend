from server.model.square import Square
import json

class Board:

    size = 64
    squares = []

    def __init__(self, id=None):
        squares = []

    def initialize(self):
        squares = []
        for x in range(self.size):
            square = Square(x)
            squares.append(square)

    def open(self,id):
        self.squares[id].open = True

    def flag(self,id):
        self.squares[id].image = 'flag'

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


