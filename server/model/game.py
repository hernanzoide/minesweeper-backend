from server.model.board import Board, PlayerBoard

class Game:

    maxMines = 9
    size= 8

    def __init__(self,id):
        self.gameOver = False
        self.board = Board(id)
        self.playerBoard = PlayerBoard(id)
        self.boardSize = Game.size * Game.size
        Board.size = self.boardSize
        Board.maxMines = Game.maxMines
        PlayerBoard.size = self.boardSize
        self.initialize()

    def initialize(self):
        self.gameOver = False
        self.playerBoard.flags = Game.maxMines
        self.playerBoard.remaining = self.boardSize-Game.maxMines
        self.board.initialize()
        self.playerBoard.initialize()

    def open(self,id):
        if (self.board.squares[id].image == 'mine'):
            self.gameOver = True
        if (self.board.squares[id].image == 'mine0'):
            self.recursivelyOpen(id)
        else:
            self.playerBoard.open(id,self.board.squares[id].image)
        
    def recursivelyOpen(self,i):
        self.playerBoard.open(i,self.board.squares[i].image)
        if (i-self.size>=0):
            if not self.playerBoard.squares[i-self.size].open:
                if self.board.squares[i-self.size].image == 'mine0':
                    self.recursivelyOpen(i-self.size)
                else:
                    self.playerBoard.open(i-self.size,self.board.squares[i-self.size].image)
        if (i+self.size<=self.boardSize-1):
            if not self.playerBoard.squares[i+self.size].open:
                if self.board.squares[i+self.size].image == 'mine0': 
                    self.recursivelyOpen(i+self.size)
                else:
                    self.playerBoard.open(i+self.size,self.board.squares[i+self.size].image)
                
        if (i) % self.size != 0:
            if i>0:
                if not self.playerBoard.squares[i-1].open:
                    if self.board.squares[i-1].image == 'mine0':
                        self.recursivelyOpen(i-1)
                    else:
                        self.playerBoard.open(i-1,self.board.squares[i-1].image)

            if i-self.size>0:
                if not self.playerBoard.squares[i-self.size+1].open:
                    if self.board.squares[i-self.size+1].image == 'mine0': 
                        self.recursivelyOpen(i-self.size+1)
                    else:
                        self.playerBoard.open(i-self.size+1,self.board.squares[i-self.size+1].image)

            if i+self.size-1<self.boardSize-1:
                if not self.playerBoard.squares[i+self.size-1].open:
                    if self.board.squares[i+self.size-1].image == 'mine0':
                        self.recursivelyOpen(i+self.size-1)
                    else:
                        self.playerBoard.open(i+self.size-1,self.board.squares[i+self.size-1].image)

        if (i) % self.size != self.size-1:
            if i<self.boardSize-1:
                if not self.playerBoard.squares[i+1].open:
                    if self.board.squares[i+1].image == 'mine0':
                        self.recursivelyOpen(i+1)
                    else:
                        self.playerBoard.open(i+1,self.board.squares[i+1].image)

            if i-self.size-2>0:
                if not self.playerBoard.squares[i-self.size-1].open:
                    if self.board.squares[i-self.size-1].image == 'mine0': 
                        self.recursivelyOpen(i-self.size-1)
                    else:
                        self.playerBoard.open(i-self.size-1,self.board.squares[i-self.size-1].image)

            if i+self.size+1<self.boardSize-1:
                if not self.playerBoard.squares[i+self.size+1].open:
                    if self.board.squares[i+self.size+1].image == 'mine0': 
                        self.recursivelyOpen(i+self.size+1)
                    else:
                        self.playerBoard.open(i+self.size+1,self.board.squares[i+self.size+1].image)

    def flag(self,id):
        print
        if self.playerBoard.squares[id].image == 'square':
            self.playerBoard.flag(id)
        else:
            self.playerBoard.unflag(id)

    def getPlayerInfo(self):
        #return remaining flags
        #self.playerBoard.flags
        #return remaining cells
        #self.playerBoard.remaining
        #return gameOver
        if self.gameOver:
            return self.board
        return self.playerBoard