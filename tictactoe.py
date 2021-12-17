from board import Board
from math import inf as infinity
from random import choice

class TicTacToe:
    def __init__(self,board,comp_choice,human_choice) -> None:
        self.__board = board
        self.__comp_choice = comp_choice
        self.__human_choice = human_choice

    def start (self,flag):
        self.__board.draw()
        if flag : 
            for i in range(9):
                if i%2 == 0 :
                    print('Human trun ',self.__human_choice)
                    pos = int(input('enter target cell number:\n'))
                    while not self.__board.set_cell(pos,self.__human_choice):
                        pos = int(input('enter target cell number:\n'))
                        if not pos in range(1,10):
                            print('out of range.')
                            exit()
                else:
                    print('Computer trun ',self.__comp_choice)
                    
                    move = self.minimax(self.__board.get_board(), len(self.__board.empty_cells()), self.__comp_choice)
                    x, y = move[0], move[1]
                    
                    self.__board.set_cell_xy(x,y,self.__comp_choice) 
                if self.__board.game_over():
                    self.__board.draw()
                    self.__board.print_winner()
                    exit()
                self.__board.draw()
                

        else:
            for i in range(9):
                if i%2 != 0 :
                    print('Human trun ',self.__human_choice)
                    pos = int(input('enter target cell number:\n'))
                    while not self.__board.set_cell(pos,self.__human_choice):
                        pos = int(input('enter target cell number:\n'))
                        if not pos in range(1,10):
                            print('out of range.')
                            exit()
                else:
                    print('Computer trun ',self.__comp_choice)
                    if i ==0: 
                        x = choice([0, 1, 2])
                        y = choice([0, 1, 2])
                        self.__board.set_cell_xy(x,y,self.__comp_choice) 
                    else:
                        
                        
                        move = self.minimax(self.__board.get_board(), len(self.__board.empty_cells()), self.__comp_choice)
                        x, y = move[0], move[1]
                        
                        self.__board.set_cell_xy(x,y,self.__comp_choice) 
                if self.__board.game_over():
                    self.__board.draw()
                    self.__board.print_winner()
                    
                    exit()    
                    
                    
                self.__board.draw()

    def minimax(self,state, depth, player):
 
        if player == self.__comp_choice:
            best = [-1, -1, -infinity]
        else:
            best = [-1, -1, +infinity]
        b = Board(state)
        if depth == 0 or b.game_over():
            score = b.evaluate(self.__comp_choice,self.__human_choice)
            return [-1, -1, score]

        for cell in b.empty_cells():
            x, y = cell[0], cell[1]
            state[x][y] = player
            score = self.minimax(state, depth - 1, self.switch(player))
            state[x][y] = 0
            score[0], score[1] = x, y

            if player == self.__comp_choice:
                if score[2] > best[2]:
                    best = score  
            else:
                if score[2] < best[2]:
                    best = score  

        return best

    def switch(self,player):
            if player == self.__comp_choice : return self.__human_choice
            return self.__comp_choice

        

