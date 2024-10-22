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

def gameLoop():
    if random.randint(0,1) == 1:
        print("You will be 'X' and the Computer will be 'O'")
        player = "X"
    else:
        print("You will be 'O' and the Computer will be 'X'")
        player = "O"

    print("X's go first: ")

    if player.upper() == "X":
        try:
            playerMove = int(input("What is your first move? "))
        except:
            print("Invalid move! Please enter a number 1 - 9")
        finally:

    else:
        computerMove = 4

