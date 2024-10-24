"""
Richard Malstrom
CMSC-1380

This code will play a game of tic-tac-toe game against a human player.

Date Last Modified: 10.22.2024
"""
import random
board = [None, None, None, None, None, None, None, None, None]

def emptyspot(space):
    if board[space] is None:
        return True
    else:
        return False
def printBoard():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--------------------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--------------------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def gameLoop():
    if random.randint(0,1) == 0:
        print("You will be 'X' and the Computer will be 'O'")
        player = "X"
        computerSymbol = "O"
    else:
        print("You will be 'O' and the Computer will be 'X'")
        player = "O"
        computerSymbol = "X"

    print("X's go first: ")


    if player == "X":
        gameOutline = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
    else:
        gameOutline = ["O", "X", "O", "X", "O", "X", "O", "X", "O"]

    for play in gameOutline:
        if play == player:
            validPlay = False
            while not validPlay:
                playerMove = int(input("Which spot would you like to take? (0 - 8):"))
                if emptyspot(playerMove):
                    board[playerMove] = player
                    validPlay = True
                else:
                    print("Invalid move: Spot already taken")
        else:
            computerMove(computerSymbol)

def computerMove(computerSymbol):
    # Currently Randomized Moves
    print("Computer move")
    move = random.randint(0,8)
    invalidMove =  True
    while invalidMove:
        if emptyspot(move):
            board[move] = computerSymbol
            invalidMove = False
printBoard()
gameLoop()

