"""
Tic Tac Toe Player
"""

import math
#import numpy as np
# importing "copy" for copy operations
import copy


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
    numberOfEmpty = sum(x.count(EMPTY) for x in board)
    if numberOfEmpty == 0:
        user = EMPTY
    elif (numberOfEmpty % 2) == 0:
        user = O
    else :
        user = X

    return user


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibleActions.append((i,j))
    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)
    if board[action[0]][action[1]] == EMPTY:
        newBoard[action[0]][action[1]] = player(board)

    return newBoard

    
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        if board[i].count(X) == 3 or (board[0][i] == X and board[1][i] == X and board[2][i] == X):
            return X
        elif board[i].count(O) == 3 or (board[0][i] == O and board[1][i] == O and board[2][i] == O):
            return O

    if board[1][1] == X and ((board[0][0] == X and board[2][2] == X) or (board[0][2] == X and board[2][0] == X)):
        return X
    elif board[1][1] == O and ((board[0][0] == O and board[2][2] == O) or (board[0][2] == O and board[2][0] == O)):
        return O

    return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    hasWinner = winner(board) != None
    if hasWinner or sum(x.count(EMPTY) for x in board) == 0:
        return True
    else:
        return False
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    gameWinner = winner(board)
    if gameWinner == X:
        return 1
    elif gameWinner == O:
        return -1
    else:
        return 0
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        possibleActions = actions(board)
        if len(possibleActions) == 1:
            return possibleActions[0]
            
        user = player(board)
        move = None
        score = 0
        if user == X:
            score = -99999
        else:
            score = 99999

        for action in possibleActions:
            newboard = result(board,action)
            if user == X:
                s = maxvalue(newboard)
                if int(s) > int(score):
                    score = s
                    move = action
            else:
                s = minvalue(newboard)
                if int(s) < int(score):
                    score = s
                    move = action
        return move

def maxvalue(board):
    if terminal(board):
        return utility(board)

    score = -99999
    for action in actions(board):
        newboard = result(board,action)
        s = minvalue(newboard)
        if int(s) > int(score):
            score = s
    return score

def minvalue(board):
    if terminal(board):
        return utility(board)

    score = 99999
    for action in actions(board):
        newboard = result(board,action)
        s = maxvalue(newboard)
        if int(s) < int(score):
            score = s
    return score