"""
Tic Tac Toe Player
"""

import copy
import math

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

    # Count the number of X's and O's on the board
    player_x=0
    player_o=0
    # Iterate through each row and column to count moves
    for list in board:
        for j in range(0,len(list)):
            if list[j]==X:
                player_x+=1
            elif list[j]==O:
                player_o+=1
    # If X has more moves than O, it's O's turn (since X goes first)
    # Otherwise, it's X's turn
    if player_x>player_o:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Initialize an empty set to store possible moves
    possible_actions=set()
    # Iterate through each cell of the board
    for i in range(len(board)):
        for j in range(len(board[i])):
            # If the cell is empty, it's a valid move
            if board[i][j]==EMPTY:
                possible_actions.add((i,j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Create a deep copy to avoid modifying the original board
    copy_board=copy.deepcopy(board)
    # Extract row and column from the action tuple
    i,j=action
    # Check if the move is valid (cell is empty)
    if (i<3 and i>=0) and (j<3 and j>=0) and copy_board[i][j]==EMPTY:
        # Place the current player's symbol in the cell
        copy_board[i][j]=player(board=board)
        return copy_board
    else:
        # Raise exception for invalid moves
        raise Exception("invalid move")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    # Check horizontally
    for i in range(len(board)):
        number_x=0
        number_o=0
        for j in range(len(board[i])):
            if(board[i][j]==X):
                number_x+=1
            elif(board[i][j]==O):
                number_o+=1
        if number_x==3:
            return X
        elif number_o==3:
            return O

    # Check vertically
    for j in range(len(board)):
        number_x=0
        number_o=0
        for i in range(len(board[j])):
            if(board[i][j]==X):
                number_x+=1
            elif(board[i][j]==O):
                number_o+=1
        if number_x==3:
            return X
        elif number_o==3:
            return O    
    # Check diagonals
    if (board[0][0] == X and board[1][1] == X and board[2][2] == X) or (board[0][2] == X and board[1][1] == X and board[2][0] == X):
        return X
    elif (board[0][0] == O and board[1][1] == O and board[2][2] == O) or (board[0][2] == O and board[1][1] == O and board[2][0] == O):
        return O
    # No winner found
    return None
      

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(len(actions(board=board))==0) or (winner(board=board)is not None):
        return True
    else:
        return False 


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Get the winner of the board
    win = winner(board)
    # Return utility values: X=1, O=-1, tie=0
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0
        

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # If game is over, no moves available
    if terminal(board=board):
        return None
    else:
        # Get current player
        curr_player=player(board=board)
        best_action=None
        # X is maximizing player (wants highest score)
        if curr_player==X:
            best_score=float("-inf")
            for action in actions(board):
                resulted_board=result(board,action)
                score=min_value(resulted_board)
                if score>best_score:
                    best_score=score
                    best_action=action
        # O is minimizing player (wants lowest score)
        else:
            best_score=float("inf")
            for action in actions(board):
                resulted_board=result(board,action)
                score=max_value(resulted_board)
                if score<best_score:
                    best_score=score
                    best_action=action
        return best_action
        

def max_value(board):
    # Base case: if game is over, return utility
    if terminal(board=board):
        return utility(board=board)
    value=float("-inf")
    # Try each possible action and take the maximum
    for action in actions(board):
        result_board=result(board,action)
        value=max(value,min_value(result_board))
    return value


def min_value(board):
    # Base case: if game is over, return utility
    if terminal(board=board):
        return utility(board=board)
    value=float("inf")
    # Try each possible action and take the minimum
    for action in actions(board):
        result_board=result(board,action)
        value=min(value,max_value(result_board))
    return value