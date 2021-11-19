# 1 player mode (bot vs player1)

import turtle

#1 -----------------------------------------------------------------------------------------------------------
def main():
    choice = int(input('''
            Welcome to Othello
            ******************

            ==================
            |    1 Player    |
            ==================
            ==================
            |    2 Player    |
            ==================

Number of players (1/2): '''))
    if choice == 1:
        print('Loading...')
        from singleP import singlePlayer
        singlePlayer()

    elif choice == 2:
        print('Loading...')
        from doubleP import doublePlayer
        doublePlayer()

    else:
        print("ERROR: Enter the number 1 (For playing against computer) or number 2 (For playing against a friend")
main()