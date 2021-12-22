from board import Board
from math import inf as infinity
from random import choice

class TicTacToe:
    '''
        Tic-Tac-Toe game class which will operate
         the whole game.
                                                '''
    def __init__(self,board,comp_choice,human_choice) -> None:
        '''
            Class instructor with the important
             variables which the game needs to
              keeps track of.
                                                '''
        self.__board = board
        self.__comp_choice = comp_choice
        self.__human_choice = human_choice

    def start (self,first_flag,AlphaBeta):

        '''
            The main method in the class which 
             will operate the whole game with
              user's preferences.
            
            We will keep printing the board
             whenever a change happens on the board.
                                                '''

        
        self.__board.draw()

        '''
            If the user wants to start first then 
             he will choose when the counter is even
              else he will choose when odd. 
                                                '''

        if first_flag : 
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
                    if AlphaBeta:move = self.alpha_beta(self.__board.get_board(), len(self.__board.empty_cells()), self.__comp_choice,-infinity,infinity)
                        
                    else :move = self.minimax(self.__board.get_board(), len(self.__board.empty_cells()), self.__comp_choice)
                    
                    x, y = move[0], move[1]
                    
                    self.__board.set_cell_xy(x,y,self.__comp_choice) 

                '''                             
                    check if the game has ended 
                     after each move.                            
                                                ''' 
                if self.__board.game_over():
                    self.__board.draw()
                    self.__board.print_winner()
                    break

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
                        
                        
                        if AlphaBeta:move = self.alpha_beta(self.__board.get_board(), len(self.__board.empty_cells()), self.__comp_choice,-infinity,infinity)
                        
                        else :move = self.minimax(self.__board.get_board(), len(self.__board.empty_cells()), self.__comp_choice)
                        x, y = move[0], move[1]
                        
                        self.__board.set_cell_xy(x,y,self.__comp_choice) 

                '''                             
                    check if the game has ended 
                     after each move.                            
                                                ''' 
                if self.__board.game_over():
                    self.__board.draw()
                    self.__board.print_winner()
                    break    
                     
                self.__board.draw()

    def minimax(self,state, depth, player):

        '''                             
            MiniMax alprithm funtion without
             Alpha-Beta pruning.                           
                                                '''

        '''                             
            We will keep track of the final value 
             in a list called best which will be 
              returned to the recursive calls
               and the final call.
            The list contains 
             [0] row index
             [1] colmun index
             [2] best score whether its max or min
                                                '''  
        if player == self.__comp_choice:
            best = [-1, -1, -infinity]
        else:
            best = [-1, -1, +infinity]
        board = Board(state)
        if depth == 0 or board.game_over():
            score = board.evaluate(self.__comp_choice,self.__human_choice)
            return [-1, -1, score]

        for cell in board.empty_cells():
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

    def alpha_beta(self,state, depth, player,alpha,beta):
        '''                             
            MiniMax alprithm funtion with
             Alpha-Beta pruning.                           
                                                '''
        
        '''                             
            This technique is an enhancement on 
             MiniMax algorithm.

            We will keep track of alpha and beta 
             values and we will prune the leafs 
              when we sure the final value
               will not change.                         
                                                '''

        if player == self.__comp_choice:
            best = [-1, -1, -infinity]
        else:
            best = [-1, -1, +infinity]

        board = Board(state)
        if depth == 0 or board.game_over():
            score = board.evaluate(self.__comp_choice,self.__human_choice)
            return [-1, -1, score]


        for cell in board.empty_cells():
            x, y = cell[0], cell[1]
            state[x][y] = player
            score = self.alpha_beta(state, depth - 1, self.switch(player),alpha, beta)
            score[0] ,score[1] = x,y 
            state[x][y] = 0

            if player == self.__comp_choice:
                
                if score[2] > alpha:
                    alpha = score[2]
                    best = score
                    best[2] = alpha
                
            else:
                if score[2] < beta:
                    beta = score[2]
                    best = score
                    best[2] = beta
                    

            if alpha >= beta:break

        return best
            

    def switch(self,player):
        '''                             
            Utility function which will invert
             the player turn.                         
                                                '''

        if player == self.__comp_choice : return self.__human_choice
        return self.__comp_choice

        

