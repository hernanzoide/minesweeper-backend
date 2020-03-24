from server.model.square import Square
import json
import random

class PlayerBoard:

    size = 64
    maxMines = 9

    def __init__(self, ownerId=None):
        self.ownerId = ownerId
        self.squares = []
        self.flags = self.maxMines
        self.remainingCells = self.size-self.maxMines

    def initialize(self):
        self.squares = []
        for x in range(self.size):
            square = Square(x,'square')
            self.squares.append(square)

    def open(self,id,image):
        if not self.squares[id].open:
            self.remainingCells-=1
            self.squares[id].image = image
            self.squares[id].open = True

    def flag(self,id):
        if self.flags>=0:
            self.flags-=1
            self.squares[id].image = 'flag'
    
    def unflag(self,id):
        if self.squares[id].image == 'flag':
            self.flags+=1
            self.squares[id].image = 'flag'

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

class Board():

    size = 64

    def __init__(self, ownerId=None):
        self.ownerId = ownerId
        self.squares = []
        self.mineIndex = []
         
    def initialize(self):
        self.squares = []
        for x in range(self.size):
            self.squares.append(Square(x,'mine0'))
        self.mineIndex = random.sample(range(0, 63), 9)
        for i in self.mineIndex:
            self.squares[i] = Square(i,'mine')
        for x in range(self.size):
            if self.squares[x].image != 'mine':
                self.squares[x] = Square(x,'mine'+str(self.countMines(x)))

    def countMines(self,i):
        count = 0
        if (i-8>=0):
            if (self.squares[i-8].image == 'mine'):
                count+=1
        if (i+8<=63):
            if (self.squares[i+8].image == 'mine'):
                count+=1
        if (i) % 8 != 0:
            if i>0:
                if (self.squares[i-1].image == 'mine'):
                    count+=1
            if i-8>0:
                if (self.squares[i-9].image == 'mine'):
                    count+=1
            if i+7<63:
                if (self.squares[i+7].image == 'mine'):
                    count+=1
        if (i) % 8 != 7:
            if i<63:
                if (self.squares[i+1].image == 'mine'):
                    count+=1
            if i-6>0:
                if (self.squares[i-7].image == 'mine'):
                    count+=1
            if i+9<63:
                if (self.squares[i+9].image == 'mine'):
                    count+=1
        return count

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)



