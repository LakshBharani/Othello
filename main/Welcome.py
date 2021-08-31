# Welcome screen
 
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

if diff == 1:
    print("Loading...")
    import gameEz
elif diff == 2:
    print("Loading...")
    import gameHard


reserved = [(14,37),(-25,-4),(-25,37),(14,-4)]