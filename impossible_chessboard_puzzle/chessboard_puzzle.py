from random import *

def random_board():
    return choices([True,False], k = 64)

def flip(board, square):
    board[square] = not board[square]
    return board

def print_board(board):
    for i in range(64):
        print("H" if board[i] else "T", end = "\n" if (i + 1) % 8 == 0 else " ")

def parity(board):
    parity = 0;
    for index, square in enumerate(board):
        if square:
            parity ^= index
    return parity

def prisoner1(magic_square, board):
    return parity(board) ^ magic_square

def prisoner2(board):
    return parity(board)

def main():
    board = random_board()
    print("Board with coins (T = tails, H = heads): ")
    print_board(board)
    magic_square = randint(0,63)
    print(f"Jailer selected square {magic_square}")
    flipped_coin = prisoner1(magic_square, board)
    print(f"Prisoner 1 flipped coin {flipped_coin}")
    flipped_board = flip(board, flipped_coin)
    answer = prisoner2(flipped_board)
    print(f"Prisoner 2 selected square {answer}")
    print("Did prisoners walk free? {a}".format(a = answer == magic_square))
    
if __name__ == "__main__":
    main()