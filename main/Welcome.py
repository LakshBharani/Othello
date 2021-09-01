# Welcome screen

# coordinates of pieces
x = [a,b,c,d,e,f,g,h] = [-145,-105,-65,-25,15,55,95,135]
y = [0,-124,-84,-44,-4,36,76,116,156]

# Homescreen message
print('''
            Welcome to Othello
            ******************

            ##################
            #    1 Player    #
            ##################

            ##################
            #    2 Player    #
            ##################
''')
# choice given to user
diff = int(input("Number of players (1/2): "))
while diff != 1 or 2:

    # checking users choice
    if diff == 1:
        print("Loading...")
        import game1p # single player mode
        break

    elif diff == 2:
        print("Loading...")
        import game2p # two player mode
        break

    else:
        print("Invalid option...try again")
        diff = int(input("Enter difficulty level(1/2): "))


# filled coordinates
reserved_black = [(e,y[5]),(d,y[4])]
reserved_white = [(d,y[5]),(e,y[4])]