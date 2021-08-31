# Welcome screen

x = [a,b,c,d,e,f,g,h]= [0,0,0,-25,14,0,0,0]
y = [0,0,0,0,-4,37,0,0,0]

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

# user picks difficulty
if diff == 1:
    print("Loading...")
    import gameEz
elif diff == 2:
    print("Loading...")
    import gameHard

# reserved coordinates
reserved = [(e,y[5]),(d,y[4]),(d,y[5]),(e,y[4])]