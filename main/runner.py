# Runner => used to start game

# used to give color to text in terminal
# syntax: Fore.<color> + <text> + Fore.RESET
from colorama import Fore

#1 -----------------------------------------------------------------------------------------------------------
def main():
    # input with colored text
    print(Fore.LIGHTGREEN_EX + ''' 
  ____    _     _              _   _
 / __ \  | |_  | |_     ____  | | | |   ___
| |  | | | __| |  _ \  /  . \ | | | |  / _ \ 
| |__| | | |_  | | | | | \__/ | | | | | |_| |
 \____/   \__| |_| |_| \____\ |_| |_|  \___/
''' 
+ Fore.LIGHTCYAN_EX +
'''
            ==================
            |    1 Player    |
            ==================
            ==================
            |    2 Player    |
            ================== 
''' + Fore.RESET)
    choice = ""
    while choice != "1" or "2":
        choice = input("Number of players (1/2): ")
        if choice == "1" or choice == "2":
            break
        else:
            print(Fore.RED + "ERROR: Invalid option" + Fore.RESET)

    if choice == "1":
        from singleP import drawBoard
        drawBoard()

    elif choice == "2":
        from doubleP import drawBoard
        drawBoard()

    else:
        print("ERROR: Enter the number 1 (For playing against computer) or number 2 (For playing against a friend")
main()