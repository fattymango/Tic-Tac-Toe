from board import Board
from tictactoe import TicTacToe

b = Board()



human_choice ,comp_choice,first_flag = '','','' 

while not human_choice.upper() in ['X','O']:
    try:
        print('')
        human_choice = input('Choose X or O:\n ').upper()
    except (EOFError, KeyboardInterrupt):
        print('Bye')
        exit()

if human_choice == 'X': comp_choice ='O'
else : comp_choice = 'X'
while not first_flag.upper() in ['Y','N']:
    try:
        print('')
        first_flag = input('Do you want to start first?[Y/N]\n ').upper()
    except (EOFError, KeyboardInterrupt):
        print('Bye')
        exit()


ttt = TicTacToe(board=b,comp_choice=comp_choice,human_choice=human_choice)
if first_flag == 'Y':ttt.start(True)
else : ttt.start(False)
