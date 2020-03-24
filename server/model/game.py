from server.model.board import Board, PlayerBoard

class Game:

    maxMines = 9
    size= 8

    def __init__(self,id):
        self.gameOver = False
        self.board = Board(id)
        self.playerBoard = PlayerBoard(id)
        self.initialize()

    def initialize(self):
        self.board.initialize()
        self.playerBoard.initialize()

    def open(self,id):
        if (self.board.squares[id].image == 'mine'):
            gameOver = True
            self.playerBoard.open(id,self.board.squares[id].image)
            print('GAME OVER')
            #self.initialize()

        if (self.board.squares[id].image == 'mine0'):
            self.recursivelyOpen(id)
        else:
            print('OPENING'+str(id))
            self.playerBoard.open(id,self.board.squares[id].image)
        
    
    def recursivelyOpen(self,i):
        self.playerBoard.open(i,self.board.squares[i].image)
        print('OPENING'+str(i))
        if (i-8>=0):
            if not self.playerBoard.squares[i-8].open:
                if self.board.squares[i-8].image == 'mine0':
                    self.recursivelyOpen(i-8)
                else:
                    self.playerBoard.open(i-8,self.board.squares[i-8].image)
        if (i+8<=63):
            if not self.playerBoard.squares[i+8].open:
                if self.board.squares[i+8].image == 'mine0': 
                    self.recursivelyOpen(i+8)
                else:
                    self.playerBoard.open(i-8,self.board.squares[i-8].image)
                
        if (i) % 8 != 0:
            if i>0:
                if not self.playerBoard.squares[i-1].open:
                    if self.board.squares[i-1].image == 'mine0':
                        self.recursivelyOpen(i-1)
                    else:
                        self.playerBoard.open(i-8,self.board.squares[i-8].image)

            if i-8>0:
                if not self.playerBoard.squares[i-9].open:
                    if self.board.squares[i-9].image == 'mine0': 
                        self.recursivelyOpen(i-9)
                    else:
                        self.playerBoard.open(i-8,self.board.squares[i-8].image)

            if i+7<63:
                if not self.playerBoard.squares[i+7].open:
                    if self.board.squares[i+7].image == 'mine0':
                        self.recursivelyOpen(i+7)
                    else:
                        self.playerBoard.open(i-8,self.board.squares[i-8].image)

        if (i) % 8 != 7:
            if i<63:
                if not self.playerBoard.squares[i+1].open:
                    if self.board.squares[i+1].image == 'mine0':
                        self.recursivelyOpen(i+1)
                    else:
                        self.playerBoard.open(i-8,self.board.squares[i-8].image)

            if i-6>0:
                if not self.playerBoard.squares[i-7].open:
                    if self.board.squares[i-7].image == 'mine0': 
                        self.recursivelyOpen(i-7)
                    else:
                        self.playerBoard.open(i-8,self.board.squares[i-8].image)

            if i+9<63:
                if not self.playerBoard.squares[i+9].open:
                    if self.board.squares[i+9].image == 'mine0': 
                        self.recursivelyOpen(i+9)
                    else:
                        self.playerBoard.open(i-8,self.board.squares[i-8].image)



    def flag(self,id):
        self.playerBoard.flag(id)

    def unflag(self,id):
        self.playerBoard.unflag(id)

    def getPlayerInfo(self):
        #return remaining flags
        #self.playerBoard.flags
        #return remaining cells
        #self.playerBoard.remaining

        #return gameOver
        #self.board.initialize()
        return self.playerBoard