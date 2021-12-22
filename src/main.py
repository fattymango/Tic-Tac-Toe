from board import Board
from tictactoe import TicTacToe


def get_player_choice():
    '''
        Get player's choice of X or O.
                                        '''

    choice = ''
    while not choice.upper() in ['X','O']:
        try:choice = input('Choose X or O:\n ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
    if choice == 'X': comp_choice ='O'
    else : comp_choice = 'X'
    return choice,comp_choice


def play_first():
    '''
        Get player's choice of starting first.
                                            '''

    choice = ''
    while not choice.upper() in ['Y','N']:
        try:choice = input('Do you want to start first?[Y/N]\n ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
    if choice == 'Y':return True
    else : return False
    
def alpha_beta():
    '''
        Get player's choice of using Alpha-
         Beta pruning.
                                            '''

    choice = ''
    while not choice.upper() in ['Y','N']:
        try:choice = input('Do you want to use Alpha-Beta pruning?[Y/N]\n ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
    if choice == 'Y':return True
    else : return False

    
human_coice , comp_choice = get_player_choice()

'''
        Calling the Tic-Tac-Toe game class
         with player's choices.
                                            '''
TicTacToe(
            board=Board(),
            comp_choice=comp_choice,
            human_choice=human_coice

            ).start(
                    first_flag=play_first(),
                    AlphaBeta=alpha_beta()
                    )

quit_flag = False
while not quit_flag:
    quit_flag = input('press and key to quit.')
    if quit_flag != False: break
    