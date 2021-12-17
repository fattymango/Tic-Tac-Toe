
import os
import time


class Board:
    def __init__(self,board = None) -> None:
        if board: 
            self.__board = board
        else:    
            self.__board = [
                [0,0,0],
                [0,0,0],
                [0,0,0] ]
        
    def evaluate(self,c,h):
        if self.check_winner(c):return +1
        elif self.check_winner(h):return -1      
        return 0    
    def empty_cells(self):
        cells = []

        for x, row in enumerate(self.__board):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x, y])
        return cells

    def valid_move(self,x,y):
        
        if self.__board[x][y] != 0: return False
        return True 
    def set_cell_xy(self,x,y,player):


        if  self.valid_move(x,y): 
            self.__board[x][y] = player
            return True

        
        return False
        
        
    def set_cell(self,pos,player):
        
        row ,col= int(pos/3),int(pos%3)
        if col == 0 : row=row-1
        col = col-1

        if not self.valid_move(row,col): 
            print('cell is used.\n')
            return False

        self.__board[row][col] = player
        
        return True
    def check(self,x,y,z):
        flag,winner = False,None    
        s = [x,y,z]
        s = set(s)
        if len(s) == 1 and s.pop() != 0:
            flag = True
            winner = x
        return flag,winner
    def check_winner(self,player):
        for row in self.__board:
            flag,winner = self.check(row[0],row[1],row[2])
            if flag :
                if winner == player:return True

        for i in range(3):
            flag,winner = self.check(self.__board[0][i],self.__board[1][i],self.__board[2][i])
            if flag :
                if winner == player:return True
                


        flag,winner = self.check(self.__board[0][0],self.__board[1][1],self.__board[2][2])
        if flag :
                if winner == player:return True
        flag,winner = self.check(self.__board[0][2],self.__board[1][1],self.__board[2][0])
        if flag :
                if winner == player:return True

        return False
    
    def game_over(self):
        if len(self.empty_cells())==0:return True
        if self.check_winner('X') : return True
        if self.check_winner('O') : return True

        return False
        
    def draw(self):
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
        return self.__board
    def print_winner(self):
        if self.check_winner('X') :
            print('X Won!')
        elif self.check_winner('O') :
            print('O Won!')
        else:
            print('TIE!')

