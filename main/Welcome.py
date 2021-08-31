# Welcome screen

# coordinates of pieces
x = [a,b,c,d,e,f,g,h] = [-145,-105,-65,-25,15,55,95,135]
y = [0,-124,-84,-44,-4,36,76,116,156]

print('''
            Welcome to Othello
            ******************

            ##################
            #     Easy(1)    #
            ##################

            ##################
            #     Hard(2)    #
            ##################
''')
diff = int(input("Enter difficulty level(1/2): "))
while diff != 1 or 2:
    # user picks difficulty
    if diff == 1:
        print("Loading...")
        import gameEz
        break
    elif diff == 2:
        print("Loading...")
        import gameHard
        break
    else:
        print("Invalid option...try again")
        diff = int(input("Enter difficulty level(1/2): "))


# filled coordinates
reserved_black = [(e,y[5]),(d,y[4])]
reserved_white = [(d,y[5]),(e,y[4])]