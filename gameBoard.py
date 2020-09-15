import numpy as np
import subprocess as sp


class gameBoard:
    def __init__(self):
        self.emptyField = '[ ]'
        self.playerOne = '[O]'
        self.playerTwo = '[X]'
        self.playerEmpty = '   '
        self.player = ' ^ '


        row6 = [self.emptyField, self.emptyField,self.emptyField,self.emptyField,self.emptyField,self.emptyField,self.emptyField]
        row5 = [self.emptyField,self.emptyField,self.emptyField,self.emptyField,self.emptyField,self.emptyField,self.emptyField]
        row4 = [self.emptyField,self.emptyField,self.emptyField,self.emptyField,self.emptyField,self.emptyField,self.emptyField]
        row3 = [self.emptyField,self.emptyField,self.emptyField,self.emptyField,self.emptyField,self.emptyField,self.emptyField]
        row2 = [self.emptyField,self.emptyField,self.emptyField,self.emptyField,self.emptyField,self.emptyField,self.emptyField]
        row1 = [self.emptyField,self.emptyField,self.emptyField,self.emptyField,self.emptyField,self.emptyField,self.emptyField]
        prow = [self.player,self.playerEmpty,self.playerEmpty,self.playerEmpty,self.playerEmpty,self.playerEmpty,self.playerEmpty]

        self.gb = np.array([row6, row5, row4, row3, row2, row1, prow])



        self.draw(self.gb)


    def draw(self, gameBoard):
        
        print(gameBoard)

    def setMove(self, move, player):
        moveIndex = move

        if player == 1:
            self.gb[6] = self.playerEmpty
            self.gb[6,moveIndex] = self.player
            for i in range(6, -1, -1):
                if self.gb[i,moveIndex] == self.emptyField:
                    self.gb[i,moveIndex] = self.playerOne
                    break
        
        if player == 2:
            self.gb[6] = self.playerEmpty
            self.gb[6,moveIndex] = self.player
            for i in range(6, -1, -1):
                if self.gb[i,moveIndex] == self.emptyField:
                    self.gb[i,moveIndex] = self.playerTwo
                    break
                

    def rowfull(self, row):
        
        if self.gb[0,row] == self.emptyField:
            return False
        else:
            return True


    def gameEnd(self):      
        #i: Reihe von 0 von oben beginnend bis 5 (6-1) als unterste, insgesamt 6; j: Spalte von 0 von links beginnend bis 6 (7-1), insgesamt 7
        
        for i in range(6):
            for j in range(4):
                if self.gb[i, j] == self.playerOne and self.gb[i, j+1] == self.playerOne and self.gb[i, j+2] == self.playerOne and self.gb[i, j+3] == self.playerOne:
                    return 1
                elif self.gb[i, j] == self.playerTwo and self.gb[i, j+1] == self.playerTwo and self.gb[i, j+2] == self.playerTwo and self.gb[i, j+3] == self.playerTwo:
                    return 2

        for i in range(3):
            for j in range(7):
                if self.gb[i,j] == self.playerOne and self.gb[i+1, j] == self.playerOne and self.gb[i+2, j] == self.playerOne and self.gb[i+3, j] == self.playerOne:
                    return 1
                elif self.gb[i,j] == self.playerTwo and self.gb[i+1, j] == self.playerTwo and self.gb[i+2, j] == self.playerTwo and self.gb[i+3, j] == self.playerTwo:
                    return 2

        for i in range(6):
            for j in range(4):
                if self.gb[i,j] == self.playerOne and self.gb[i-1, j+1] == self.playerOne and self.gb[i-2, j+2] == self.playerOne and self.gb[i-3, j+3] == self.playerOne:
                    return 1
                elif self.gb[i,j] == self.playerTwo and self.gb[i-1, j+1] == self.playerTwo and self.gb[i-2, j+2] == self.playerTwo and self.gb[i-3, j+3] == self.playerTwo:
                    return 2

        for i in range(3):
            for j in range(4):
                if self.gb[i,j] == self.playerOne and self.gb[i+1, j+1] == self.playerOne and self.gb[i+2, j+2] == self.playerOne and self.gb[i+3, j+3] == self.playerOne:
                    return 1
                elif self.gb[i,j] == self.playerTwo and self.gb[i+1, j+1] == self.playerTwo and self.gb[i+2, j+2] == self.playerTwo and self.gb[i+3, j+3] == self.playerTwo:
                    return 2


        if self.isMovesLeft() == False:
            return 3
                


    def isMovesLeft(self):
        for i in range(7):
            if self.gb[0,i] == self.emptyField:
                return True
        return False
    


