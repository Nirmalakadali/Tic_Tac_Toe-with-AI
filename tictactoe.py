"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_count=0
    O_count=0
    for i in range(3):
        for j in range(3):
            if(board[i][j]==X):
                X_count=X_count+1
            elif(board[i][j]==O):
                O_count+=1
    if(X_count==O_count):
        return X
    else:
        return O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action=set()
    for i in range(3):
        for j in range(3):
            if(board[i][j]==EMPTY):
               action.add((i,j))
    return action
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_move = player(board)

    new_board = deepcopy(board)
    i, j = action

    if board[i][j] != None:
        raise Exception
    else:
        new_board[i][j] = player_move

    return new_board




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if(board[i][0]==board[i][1]==board[i][2]  and board[i][0]!=EMPTY):
            return board[i][0]
        if(board[0][i]==board[1][i]==board[2][i]  and board[0][i]!=EMPTY):
            return board[0][i]
    if(board[0][0]==board[1][1]==board[2][2]  and board[0][0]!=EMPTY):
            return board[0][0]
    if(board[1][1]==board[0][2]==board[2][0]  and board[2][0]!=EMPTY):
            return board[2][0]
    return None
    raise NotImplementedError


def terminal(board):
    """

    Returns True if game is over, False otherwise.
    """
    if winner(board)!=None or all(all(cell!=EMPTY for cell in row) for row in board):
        return True
    else:
        return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if(all(all(cell!=EMPTY for cell in row) for row in board)):
        return 0
    if(winner(board)=='O'):
        return -1
    if(winner(board)=='X'):
        return 1
    return None
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    
    current_player=player(board)
    def max_value(board):
        best_move=()
        if(terminal(board)==True):
            return utility(board),best_move
        else:
            v=float('-inf')
            possible_action=actions(board)
            for i,j in possible_action:
                score=min_value(result(board,(i,j)))[0]
                if score>v:
                    v=score
                    best_move=(i,j)
            return v,best_move
    def min_value(board):
        best_move=()

        if(terminal(board)==True):
            return utility(board),best_move
        else:
            v=float('inf')
            possible_action=actions(board)  
            for i,j in possible_action:
                score=max_value(result(board,(i,j)))[0]
                if score<v:
                    v=score
                    best_move=(i,j)
            return v,best_move
    if(terminal(board)):
        return None
    if current_player==X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]
    raise NotImplementedError
