from server.model.square import Square
import json

class Board:

    size = 64

    def __init__(self, ownerId=None):
        self.ownerId = ownerId
        self.squares = []

    def initialize(self):
        if (len(self.squares)==0):
            for x in range(self.size):
                square = Square(x)
                self.squares.append(square)

    def open(self,id):
        self.squares[id].image = 'open'
        self.squares[id].open = True

    def flag(self,id):
        self.squares[id].image = 'flag'

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


