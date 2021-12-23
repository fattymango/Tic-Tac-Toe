# Tic-Tac-Toe
#### Tic-Tac-Toe game using the MiniMax algorithm and Alpha-Beta pruning.
###### Wrote using Python, every game element is an class so it can be reusable for other projects!
###### This is a project for my AI class #CS362.
## Installation
1. First click **Code** green button 
<p align="center">
<img src="/imgs/code.png" width="350" >
</p>

2. Click **Download ZIP** button
<p align="center">
<img src="/imgs/install.png" width="350" >
</p>

3. Extract the files.
4. Open **main.exe** and enjoy!


## How to play
1. Make sure you've opened **main.exe** 
2. The game will ask you what player you would like to choose (X or O) :
<br>
<p align="center">
<img src="/imgs/xo.png" width="350" >
</p>
3. The game will ask you if you would like to start first, you can answer that by typing Y for yes and N for no :
<br><br>
<p align="center">
<img src="/imgs/first.png" width="350" >
</p>
3. The game will ask you if you would like to use Alpha-Beta pruning or not, you can answer that by typing Y for yes and N for no :
<br><br>
<p align="center">
<img src="/imgs/alphabeta.png" width="350" >
</p>
4.The game will draw a numbered board and you can choose which cell you would like to use by typing its shown number:
<br><br>
<p align="center">
<img src="/imgs/board.png" width="350" >
</p>
5.After hitting enter, the computer will make his move and draw the board again.
<br><br>
<p align="center">
<img src="/imgs/after.png" width="350" >
</p>
6. When the game ends it will print out the winner.
<br><br>
<p align="center">
<img src="/imgs/tie.png" width="350" >
</p>

**ps : You will never win. enjoy!**

## Board
```python
Board(board = None)
```
- Board class will initalize an empty board
and operate every utility function needed
to be done on the board.

- The class can accept external boards and operate the same functions on them.

## TicTacToe
```python
TicTacToe(board,comp_choice,human_choice)
```
###### Description :
    Handles the whole game from the first start until the end.
- the class takes 3 mandatory arguments:
    1. ```board``` 
        - this arguments must be  a ```Board()``` object thus the game can operate on. 
    2. ```comp_choice``` 
        - ```[char]``` the choice of the Computer whether its X or O.
    3. ```human_choice``` 
        - ```[char]``` the choice of the Human whether its X or O.
    
#### start()
```python 
start(first_flag,AlphaBeta)
```
###### Description :
    Handles the whole game process and works out user's preferences.
- it takes 2 mandatory arguments:
    1. ```first_flag``` 
        - ```[bool]``` determines if the user wants to start first.
    2. ```AlphaBeta``` 
        - ```[bool]``` determines if the user wants to use Alpha-Beta pruning.

## minimax()
```python 
minimax(state, depth, player)
```
###### Description :
    Determines the AI next move by using the basic MiniMax algorithm.
- it takes 3 mandatory arguments:
    1. ```state``` 
        - ```[list]``` A list object which represents the current state of the board.
    2. ```depth``` 
        - ```[int]``` current depth of the search tree.
    3. ```player``` 
        - ```[char]``` current player turn.
###### Technique :
The function first initializes a default value to start looping through the tree.
```python 
if player == self.__comp_choice:
    best = [-1, -1, -infinity]
else:
    best = [-1, -1, +infinity]
```
while ```best [list]``` represents the best move the function have explored yet in
```[row , column , score] ```
 format then we will create a temporary
``` Board()``` object so we can use its utility functions.
```python
board = Board(state)
```
if the game has ended or the depth is 0 then we have encountered a leaf node and we will evaluate its score 
```python 
if depth == 0 or board.game_over():
  score = board.evaluate(self.__comp_choice,self.__human_choice)
  return [-1, -1, score]
```

```evaluate()``` will return the terminal leaf value.
- if AI wins return 1
- if human wins return -1
- if its a tie return 0
    
    
```python
evaluate(self,c,h):

if self.check_winner(c):return +1
elif self.check_winner(h):return -1      
return 0    
```

to get to the state of leaf node we need to create the tree by looping through every possible move of the current state of board
we will lopp recursively by calling the ```minimax``` function and decreasing the depth : 
```python 
for cell in board.empty_cells():
    x, y = cell[0], cell[1]
    state[x][y] = player
    score = self.minimax(state, depth - 1, self.switch(player))
    state[x][y] = 0
    score[0], score[1] = x, y
```
then we will compare the score of the leaf node with our best current score and choose which is better whether the current player is maximizing or minimizing:
```python 
if player == self.__comp_choice:
  if score[2] > best[2]:
    best = score  
else:
  if score[2] < best[2]:
    best = score  
```
At the end of the call we will return our best position and score
```python 
return best
```
## alpha-beta
```python 
alpha_beta(state, depth, player,alpha,beta)
```
###### Description :
    Determines the AI next move by using the enhanced MiniMax algorithm.
    this functions has a slight difference of the basic minimax function with huge performance gap,
    tracking alpha and beta values allow us to determine whether the next unexplored branches and leafs are useless and won't
    affect our score or not, if is then we won't explore them.
- it takes 5 mandatory arguments:
    1. ```state``` 
        - ```[list]``` A list object which represents the current state of the board.
    2. ```depth``` 
        - ```[int]``` An integer which represents the current depth of the search tree.
    3. ```player``` 
        - ```[char]``` A character which represents the current player turn.
    4. ```alpha``` 
        - ```[int]``` the current alpha value.
    5. ```beta``` 
        - ```[int]``` the current beta value.
###### Technique :
As i mentioned before there is a slight difference between ``` alpha_beta() ``` and ``` minimax() ```.
Since we are tracking the alpha beta values then we will keep comparing their values with our best score.
If alpha is finally bigger than beta then we can break the loop and return the value.
```python 
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


```
## requirements 
* python 3.0+
