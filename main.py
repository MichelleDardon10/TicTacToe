'''
Tic-tac-toe game utils.

'''


def create_empty_board():

    board = []
    for i in range(3):
        board.append([None] * 3)

    return board


def print_board(board):

    print('\n'.join([str(row) for row in board]))


def update_board(board,player):
    
    for i in range(9):

        position1 = int(input("Ingrese fila: "))
        position2 = int(input("Ingrese columna: "))

        player = int(input("1 for X/ 0 for O: "))

        board[position1][position2] = player

        print('\n'.join([str(row) for row in board]))

        
    



def check_for_winner(board):
    
    if (board[0][0] == board [1][0] == board[2][0]):
        print ("X wins")
    elif (board[0][1]== board [1][1] == board[2][1]):
        print("X wins")
    elif (board[0][2] == board[1][2]== board[2][2]):
        print("X wins")
    elif (board[0][0]== board [0][1] == board[0][2]):
        print("X wins")
    elif (board[1][0]== board [1][1] == board[1][2]):
        print("X wins")
    elif (board[2][0]== board [2][1] == board[2][2]):
        print("X wins")
    elif (board[0][0]== board [1][1] == board[2][2]):
        print("X wins")
    elif (board[2][0]== board [1][1] == board[0][2]):
        print("X wins")
    else:
        print("O wins")






'''
Testing: 
'''
board = create_empty_board()
print_board(board)
movida = update_board(board,1)
check_for_winner(board)