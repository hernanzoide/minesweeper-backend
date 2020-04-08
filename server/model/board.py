from server.model.square import Square
import json
import random

class PlayerBoard:

    size = 64
    maxMines = 9

    def __init__(self, ownerId=None):
        self.ownerId = ownerId
        self.squares = []
        self.flags = PlayerBoard.maxMines
        self.remainingCells = PlayerBoard.size-PlayerBoard.maxMines

    def initialize(self):
        self.squares = []
        self.flags = self.maxMines
        for x in range(self.size):
            square = Square(x,'square')
            self.squares.append(square)

    def open(self,id,image):
        if not self.squares[id].open:
            self.remainingCells-=1
            self.squares[id].open = True
            self.squares[id].image = image

    def flag(self,id):
        if self.flags>0 and self.squares[id].image == 'square' :
            self.flags-=1
            self.squares[id].image = 'flag'
    
    def unflag(self,id):
        if self.squares[id].image == 'flag':
            self.flags+=1
            self.squares[id].image = 'square'

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

class Board():

    size = 8

    def __init__(self, ownerId=None):
        self.ownerId = ownerId
        self.squares = []
        self.mineIndex = []
        self.boardSize = Board.size * Board.size
         
    def initialize(self):
        self.squares = []
        for x in range(self.boardSize):
            self.squares.append(Square(x,'mine0'))
        self.mineIndex = random.sample(range(0, self.boardSize-1), self.maxMines)
        for i in self.mineIndex:
            self.squares[i] = Square(i,'mine')
        for x in range(self.boardSize):
            if self.squares[x].image != 'mine':
                self.squares[x] = Square(x,'mine'+str(self.countMines(x)))

    def countMines(self,i):
        count = 0
        if (i-self.size>=0):
            if (self.squares[i-self.size].image == 'mine'):
                count+=1
        if (i+self.size<=self.boardSize-1):
            if (self.squares[i+self.size].image == 'mine'):
                count+=1
        if (i % self.size) != 0:
            if i>0:
                if (self.squares[i-1].image == 'mine'):
                    count+=1
            if i-self.size>0:
                if (self.squares[i-self.size-1].image == 'mine'):
                    count+=1
            if i+self.size-1<self.boardSize-1:
                if (self.squares[i+self.size-1].image == 'mine'):
                    count+=1
        if (i % self.size) != self.size-1:
            if i<self.boardSize-1:
                if (self.squares[i+1].image == 'mine'):
                    count+=1
            if i-self.size+1>0:
                if (self.squares[i-self.size+1].image == 'mine'):
                    count+=1
            if i+self.size+1<self.boardSize-1:
                if (self.squares[i+self.size+1].image == 'mine'):
                    count+=1
        return count

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)



