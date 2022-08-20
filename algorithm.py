"""
Tic Tac Toe Player
"""

import math
import copy
import random

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
    x = 0
    o = 0
    for i in range(3):
        for j in range (3):
            if board[i][j] == X:
                x+=1
            elif board[i][j] == O: 
                o+=1

    if board == initial_state():
        return X
    else:
        if x > o:
            return (O)
        else:

            return (X)

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action.add((i, j))
    return (action)

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise NameError('not an available action')
    copyl = copy.deepcopy(board)
    copyl[action[0]][action[1]] = player(copyl)
    return (copyl)
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """         
    for i in range(3):
        if board [i][0] == board [i][1] == board [i][2] is not None:
            return board[i][0]
    for i in range(3):
        if board [0][i] == board [1][i] == board [2][i] is not None:
            return board[0][i]
    if board [0][0] == board [1][1] == board [2][2] is not None:
            return board[0][0]
    if board [0][2] == board [1][1] == board [2][0] is not None:
            return board[0][2]
    return None
    
    raise NotImplementedError
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    ctr = 0
    for i in range (3):
        for j in range (3):
            if board [i][j]== EMPTY:
                ctr +=1
    if ctr == 0:
        return True
    if winner(board) == X or winner(board) == O:
        return True
    return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return (int(1))
    elif winner(board) == O:
        return (int(-1))
    else:
        return (int(0))

    raise NotImplementedError


def maxv(board):
    v = - math.inf
    act = (None,None)
    best = -1
    if terminal(board):
        return (utility(board), act)
    for action in actions(board):
        v = max(v,(minv(result(board,action))[0]))
        if v == 1:
            act = action
            return (v,act)
        elif v == 0:
            best = 0
            act = action
        else:
            if best == -1:
                act = action
    return (v,act)

def minv(board):
    v = math.inf
    act = (None,None)
    best = 1
    if terminal(board):
        return (utility(board), act)
    for action in actions(board):
        v = min(v,(maxv(result(board,action))[0]))
        if v == -1:
            act = action
            return (v,act)
        elif v == 0:
            best = 0
            act = action
        else:
            if best == 1:
                act = action

    return (v,act)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    move = (None,None)
    if terminal(board):
        return None
    

    if player(board) == X:
        best = -math.inf
        for action in actions(board):
            board[action[0]][action[1]] = X
            v = minv(board)[0]
            board[action[0]][action[1]] = EMPTY
            if v > best:
                move = action
                best = v
        return move

    elif player(board)==O: 
        best = math.inf
        for action in actions(board):
            board[action[0]][action[1]] = O
            v = maxv(board)[0]
            board[action[0]][action[1]] = EMPTY
            if v < best:
                move = action
                best = v
        return move
            


    raise NotImplementedError
