
import algorithm as alg
X = "X"
O = "O"
EMPTY = None
User = None
ai = False
#ask the user if he is gonna play with x or o

board = alg.initial_state()
def user():
    user = input("Do you want to play with X or O? ")
    if user == "X" or user == "x":
        return X
    if user == "O" or user == "o":
        return O
    else:
        print("Invalid input. Try again.")
        user()


def user_move(board):
    
    while True:
        move = [None,None]
        move[0] = int(input("Enter the row(0-2): "))
        move[1] = int(input("Enter the column(0-2): "))
        move = (move[0], move[1])
        if move in alg.actions(board):
            return move
        else:
            print("Invalid move. Try again.")

def draw_board(board):
    for i in range(3):
        print("-------------")
        for j in range(3):
            print("|", end=" ")
            if board[i][j] == X:
                print(X, end=" ")
            elif board[i][j] == O:
                print(O, end=" ")
            else:
                print(" ", end=" ")
        print("|")
    print("-------------")
    

while (alg.terminal(board) == False):
    
    if User is None:
        User = user()
    else:
        player = alg.player(board)
        if User != player:
            if ai:
                move = alg.minimax(board)
                board = alg.result(board, move)
                ai= False
            else:
                ai = True
        if User == player:
            move = user_move(board)
            board = alg.result(board, move)
        draw_board(board)

draw_board(board)
winner = alg.winner(board)
if winner is None:
    print("Game Over: Tie.")
else:
    print(f"Game Over: {winner} wins.")
