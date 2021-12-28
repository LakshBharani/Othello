# Runner => used to start game

# used to give color to text in terminal
# syntax: Fore.<color> + <text> + Fore.RESET
from colorama import Fore

#1 -----------------------------------------------------------------------------------------------------------
def main():
    # input with colored text
    choice = int(input(Fore.LIGHTMAGENTA_EX + ''' 
            Welcome to Othello''' + Fore.RED + '''
            ******************''' + Fore.LIGHTCYAN_EX +
'''
            ==================
            |    1 Player    |
            ==================
            ==================
            |    2 Player    |
            ==================
''' + Fore.RESET + '''
Number of players (1/2): '''))
    if choice == 1:
        from singleP import drawBoard
        drawBoard()

    elif choice == 2:
        from doubleP import drawBoard
        drawBoard()

    else:
        print("ERROR: Enter the number 1 (For playing against computer) or number 2 (For playing against a friend")
main()
print()