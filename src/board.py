import os
import time


class Board:
    '''
        Board class will initalize an empty board
         and operate every utility function needed
          to be done on the board.
                                                '''

    def __init__(self,board = None) -> None:
        '''
            Class instructor will keep track 
             of the board state.

            The class can accept other board and 
             operate the same functions on it. 
                                                '''

        if board: 
            self.__board = board
        else:    
            self.__board = [
                [0,0,0],
                [0,0,0],
                [0,0,0] ]
        
    def evaluate(self,c,h):
        '''
            Evaluation function which will return 
             the terminal leaf value.
            if AI wins return 1
            if human wins return -1
            if its a tie return 0
                                                '''

        if self.check_winner(c):return +1
        elif self.check_winner(h):return -1      
        return 0    
    def empty_cells(self):
        '''
            A utility function which will return every 
             possible move of the current state of
              the board.
                                                '''
        cells = []
        for x, row in enumerate(self.__board):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])
        return cells

    def valid_move(self,x,y):
        '''
            A utility function which will check if
             if the proposed move is valid or not.
                                                '''
        if self.__board[x][y] != 0: return False
        return True 
    def set_cell_xy(self,x,y,player):
        '''
            A utility function which will assign the 
             player value on the board.
            
            this function will use the raw Row and Column
             positions which will be used more from the 
              AI.
                                                '''

        if  self.valid_move(x,y): 
            self.__board[x][y] = player
            return True

        
        return False
        
        
    def set_cell(self,pos,player):
        '''
            A utility function which will assign the 
             player value on the board.
            
            this function will use a dynamic position
             which will be used more from the user.
                                                '''
        row ,col= int(pos/3),int(pos%3)
        if col == 0 : row=row-1
        col = col-1

        if not self.valid_move(row,col): 
            print('cell is used.\n')
            return False

        self.__board[row][col] = player
        
        return True
    def check(self,x,y,z):
        '''
            A utility function which will check if 
             the row or column or diagonal values are
              the same value and not 0.
            
            the technique used here is by using a Set()
             which will keep only unique values in it 
              by appending the values to the set and 
               checking the length.

            if the length is 1 then we will check if 
             the value is 0, if not then we have a winner.
                                                        '''
        flag,winner = False,None    
        s = [x,y,z]
        s = set(s)
        if len(s) == 1 and s.pop() != 0:
            flag = True
            winner = x
        return flag,winner

    def check_winner(self,player):
        '''
            A utility function which will check if 
             the target player has won.
        
            the function will loop through each 
             column and row and diagonal values.
                                                '''
        # check all rows.
        for row in self.__board:
            flag,winner = self.check(row[0],row[1],row[2])
            if flag :
                if winner == player:return True

        # check all columns.
        for i in range(3):
            flag,winner = self.check(self.__board[0][i],self.__board[1][i],self.__board[2][i])
            if flag :
                if winner == player:return True
                

        # check all diagonal values.
        flag,winner = self.check(self.__board[0][0],self.__board[1][1],self.__board[2][2])
        if flag :
                if winner == player:return True
        flag,winner = self.check(self.__board[0][2],self.__board[1][1],self.__board[2][0])
        if flag :
                if winner == player:return True
    # if no one wins the return false.
        return False
    
    def game_over(self):
        '''
            A utility function which will check if 
             the game has finished  by checking
            if any of the players has won or its 
             a tie.
                                                '''
        if len(self.empty_cells())==0:return True
        if self.check_winner('X') : return True
        if self.check_winner('O') : return True

        return False
        
    def draw(self):
        '''
            This function will draw a readable 
             representation of the  current state
              of the board.  
                                                '''
        time.sleep(0.1)
        os.system('cls')
        counter = 1
        for row in self.__board:
            a,b,c = row[0],row[1],row[2]
            if a == 0 : a = counter
            if b == 0 : b = counter+1
            if c == 0 : c = counter+2
            print(str(a)+' | '+str(b)+' | '+str(c))
            counter = counter+3
        print()
        time.sleep(0.3)

    def get_board (self):
        # returns the board.
        return self.__board
    def print_winner(self):
        '''
            This function will determine whether 
             on of the players has won or a tie
              and print it out.
                                                '''
        if self.check_winner('X') :
            print('X Won!')
        elif self.check_winner('O') :
            print('O Won!')
        else:
            print('TIE!')

