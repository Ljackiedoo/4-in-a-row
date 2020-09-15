import subprocess as sp
import gameBoard
from copy import deepcopy
import math



class manager:
    def __init__(self):

        self.startGame()

        


    def startGame(self):
        playchoice = input("Welcome to '4 in a row': Do you want to play against another Player (1) or the CPU (2)? 1/2")
        if playchoice == "1":
            self.computer = False
        elif playchoice == "2":
            self.computer = True
        else:
            print("Please choose one of the given options!")
            self.startGame()

        input("Press a Key to start the game")

        sp.call('cls',shell=True)
        
        self.gameEnded = False

        self.gameboard = gameBoard.gameBoard()

        

        while self.gameEnded == False:
            self.playerOneMove()
            if self.gameEnd() == True:
                break
            self.playerTwoMove()
            if self.gameEnd() == True:
                break
        self.playAgain()


    def playAgain(self):
        playagain = input("Do you want to play again? y/n")
        if playagain == "y":
            self.startGame()
        elif playagain == "n":
            quit()
        else:
            print("Please enter one of the given options!")
            self.playAgain()


            
        
    def playerOneMove(self):
        playerPos = input()
        player = 1

        if playerPos.isdigit() and (int(playerPos) > 0 and int(playerPos) < 8 ):
            
            if self.gameboard.rowfull(int(playerPos)-1) == False:
                self.gameboard.setMove(int(playerPos)-1, player)
                
                self.gameboard.draw(self.gameboard.gb)
            else:
                print("Please choose a different column!")
                self.gameboard.draw(self.gameboard.gb)
                self.playerOneMove()
        else:
            print("Please choose a Number between 1 and 7")
            self.gameboard.draw(self.gameboard.gb)
            self.playerOneMove()

    def playerTwoMove(self):

        
        player = 2



        if self.computer == True:

            depth = 4
            
            gb_copy = deepcopy(self.gameboard)
        


            move = self.findBestMove(gb_copy, depth)

            

            self.gameboard.setMove(move,player)
            self.gameboard.draw(self.gameboard.gb)

            
        else:

            playerPos = input()

            if playerPos.isdigit() and (int(playerPos) > 0 and int(playerPos) < 8 ):
                
                if self.gameboard.rowfull(int(playerPos)-1) == False:
                    self.gameboard.setMove(int(playerPos)-1, player)
                    
                    self.gameboard.draw(self.gameboard.gb)
                else:
                    print("Please choose a different column!")
                    self.gameboard.draw(self.gameboard.gb)
                    self.playerTwoMove()
            else:
                print("Please choose a Number between 1 and 7")
                self.gameboard.draw(self.gameboard.gb)
                self.playerTwoMove()


    def gameEnd(self):
        if self.gameboard.gameEnd() == 1:
            print("Player 1 won!")
            self.gameEnded = True
            return True
        elif self.gameboard.gameEnd() == 2:
            print("Player 2 won!")
            self.gameEnded = True
            return True
        elif self.gameboard.gameEnd() == 3:
            print("Draw!")
            self.gameEnded = True
            return True



    def findBestMove(self, board, depth):
        
        bestVal = -1000
        bestMoveColumn = 0

        alpha = -1000
        beta = 1000
        

        #i = Reihen von oben nach unten, j = Spalte von links nach rechts
        for i in range(6):
            for j in range(7):
                if board.rowfull(j) == True:
                        continue
                if board.gb[i,j] == board.emptyField and (board.gb[i+1, j] == board.player or board.gb[i+1, j] == board.playerEmpty or board.gb[i+1, j] == board.playerOne or board.gb[i+1, j] == board.playerTwo):
                    
                    board.gb[i,j] = board.playerTwo

                    moveVal = self.minimax(board, 0, depth, False, alpha, beta)

                    board.gb[i,j] = board.emptyField

                    if moveVal > bestVal:
                        bestVal = moveVal
                        bestMoveColumn = j

        return bestMoveColumn


    def minimax(self,board,currentdepth, targetdepth, isMaximizer, alpha, beta):

        bestmoveval = self.evaluate(board)

        end = False

        if bestmoveval == -50:
            return bestmoveval + currentdepth
        elif bestmoveval == 50:
            return bestmoveval - currentdepth
        elif board.isMovesLeft() == False:
            return bestmoveval
        elif currentdepth == targetdepth:
            return bestmoveval

        if isMaximizer == True:

            best = -1000

            for i in range(6):
                for j in range(7):
                    if board.rowfull(j) == True:
                            continue
                    if board.gb[i,j] == board.emptyField and (board.gb[i+1, j] == board.player or board.gb[i+1, j] == board.playerEmpty or board.gb[i+1, j] == board.playerOne or board.gb[i+1, j] == board.playerTwo):
                        
                        board.gb[i,j] = board.playerTwo

                        best = max(best, self.minimax(board, currentdepth+1, targetdepth, False, alpha, beta))

                        board.gb[i,j] = board.emptyField

                        alpha = max(alpha, best)

                        if beta <= alpha:
                            end = True
                            break
                if end == True:
                    break
                    
            return best
        
        else:

            best = 1000

            for i in range(6):
                for j in range(7):
                    if board.rowfull(j) == True:
                            continue
                    if board.gb[i,j] == board.emptyField and (board.gb[i+1, j] == board.player or board.gb[i+1, j] == board.playerEmpty or board.gb[i+1, j] == board.playerOne or board.gb[i+1, j] == board.playerTwo):
                        
                        board.gb[i,j] = board.playerOne

                        best = min(best, self.minimax(board, currentdepth+1, targetdepth, True, alpha, beta))

                        board.gb[i,j] = board.emptyField

                        beta = min(beta, best)

                        if beta <= alpha:
                            end = True
                            break
                if end == True:
                    break
                    
            return best


            
    def evaluate(self, board):
        if board.gameEnd() == 1:
            return -50
        elif board.gameEnd() == 2:
            return 50
        else:
            return 0

        

        

        




manager()