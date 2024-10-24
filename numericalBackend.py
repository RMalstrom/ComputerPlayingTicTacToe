"""
Richard Malstrom
CMSC-1380

This code will play a game of tic-tac-toe game against a human player.

Date Last Modified: 10.22.2024

-1 = x
1 = o
"""
import random
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# board = ["", "", "", "", "", "", "", "", ""]

def emptyspot(space):
    if board[space] is 0:
        return True
    else:
        return False

def printBoard():
    modBoard = [None, None, None, None, None, None, None, None, None]
    
    for i in board:
        if i == -1:
            modBoard[i] = "X"
        elif i == 1:
            modBoard[i] = "O"
        else:
            modBoard[i] = None
    
    print(f"{modBoard[0]} | {modBoard[1]} | {modBoard[2]}")
    print("--------------------")
    print(f"{modBoard[3]} | {modBoard[4]} | {modBoard[5]}")
    print("--------------------")
    print(f"{modBoard[6]} | {modBoard[7]} | {modBoard[8]}")

def gameLoop():
    if random.randint(0,1) == 0:
        print("You will be 'X' and the Computer will be 'O'")
        player = -1
        computerSymbol = 1
    else:
        print("You will be 'O' and the Computer will be 'X'")
        player = 1
        computerSymbol = -1

    print("X's go first: ")


    if player == -1:
        gameOutline = [-1, 1, -1, 1, -1, 1, -1, 1, -1]
    else:
        gameOutline = [1, -1, 1, -1, 1, -1, 1, -1, 1]

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
        if emptyspot(move) == False:
            print("Invalid move try again")
            break
        else:
            board[move] = computerSymbol
            invalidMove = False
            printBoard()


printBoard()
gameLoop()
