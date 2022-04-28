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
    
    pass


'''
Testing: 
'''
board = create_empty_board()
print_board(board)
movida = update_board(board,1)
