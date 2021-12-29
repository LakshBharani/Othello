# 2 player mode (Player vs Computer)

import turtle
from colorama import Fore
import time

global whiteTurn
whiteTurn = True

# coordinates of pieces
global x
x = {"a":-145, "b":-105, "c":-65, "d":-25, "e":15, "f":55, "g":95, "h":135}
global y
y = {"1":-124, "2": -84, "3":-44, "4":-4, "5":36, "6":76, "7":116, "8":156}

#1 -----------------------------------------------------------------------------------------------------------
def drawBoard():
  sc = turtle.Screen()
  sc.tracer(3)

  # create turtle
  global pen
  pen = turtle.Turtle()

  # method to draw square
  def drawSquare():
    for i in range(4):
      pen.forward(40)
      pen.left(90)
    pen.forward(40)

  # screen size
  sc.setup(600, 600)

  # show rules page on turtle screen
  showRules()

# start drawing game board once rules read
  # loops for board
  for i in range(8):
    pen.up()

  # position for row
    pen.setpos(-165, -130 + 40 * i)
    pen.down()

  # coloring the squares
    for j in range(8):

      # color for squares
      col ='lightgreen'

      # fill with given color
      pen.fillcolor(col)

      # filling with colour
      pen.begin_fill()

      # method to draw square
      drawSquare()
      
      # stop filling
      pen.end_fill()
  pen.up()

  # printing numbers on y axis
  ytemp = -115
  for i in range (1,9):
    pen.setpos(-185,ytemp)
    pen.write(i)
    ytemp+=40

  # printing numbers on x axis
  xtemp = -145
  for i in range (1,9):
    pen.setpos(xtemp,-155)
    pen.write(chr(i+64))
    xtemp+=40

  def drawCircle():
    pen.down()
    pen.circle(radius=13)

  # drawing init circle(white)
  col = "white"
  pen.up()
  pen.setpos(x["e"],y["5"])
  pen.fillcolor(col)
  pen.begin_fill()
  drawCircle()
  pen.end_fill()

  pen.up()
  pen.setpos(x["d"],y["4"])
  pen.fillcolor(col)
  pen.begin_fill()
  drawCircle()
  pen.end_fill()

  # drawing init circle(black)
  col = "black"
  pen.up()
  pen.setpos(x["d"],y["5"])
  pen.fillcolor(col)
  pen.begin_fill()
  drawCircle()
  pen.end_fill()

  pen.up()
  pen.setpos(x["e"],y["4"])
  pen.fillcolor(col)
  pen.begin_fill()
  drawCircle()
  pen.end_fill()
  pen.hideturtle()

  # Placing more pieces
  startGame()

  # End editing board
  sc.update()
  turtle.mainloop()

#2 -----------------------------------------------------------------------------------------------------------
def startGame():
  empty_spaces_white = 30
  empty_spaces_black = 30

  global filled_spaces_white
  filled_spaces_white = ["d4", "e5"]
  global filled_spaces_black
  filled_spaces_black = ["d5", "e4"]

  while empty_spaces_white != 0 or empty_spaces_black != 0:
    global x_coord
    global y_coord
    global whiteTurn

    # White player's turn
    if whiteTurn == True:
      color = "white"
      print(Fore.YELLOW + "------- White -------" + Fore.RESET)
      coord = input("Enter coordinates: " + Fore.YELLOW)
      print(Fore.RESET, end="")
      if len(coord) != 0:
        x_coord = coord[0].casefold()
        y_coord = coord[1:].casefold()

        # TO DO: ADD CONDITION TO CHECK IF LEGAL MOVE (isLegal = true?) --> Nishtha
        if (x_coord+y_coord) not in filled_spaces_white and (x_coord+y_coord) not in filled_spaces_black and x_coord in x.keys() and y_coord in y.keys():
          placePiece(color, x_coord, y_coord)
          empty_spaces_white -= 1
          filled_spaces_white.append(x_coord+y_coord)
          flipPieces(color, x_coord, y_coord)
          whiteTurn = False

        # error message for placing piece on filled square  
        else:
          print(Fore.RED + "Invalid move: Try again" + Fore.RESET)

      # error message for empty input
      else:
        print(Fore.RED + "Invalid move: Try again" + Fore.RESET)

      # Black player's turn
    else:
      color = "black"
      print(Fore.BLUE + "------- Black -------" + Fore.RESET)
      coord = input("Enter coordinates: " + Fore.BLUE)
      print(Fore.RESET, end="")
      if len(coord) != 0:
        x_coord = coord[0]
        y_coord = coord[1:]

        # TO DO: ADD CONDITION TO CHECK IF LEGAL MOVE (isLegal = true?) --> Nishtha
        if (x_coord+y_coord) not in filled_spaces_black and (x_coord+y_coord) not in filled_spaces_white and x_coord in x.keys() and y_coord in y.keys():
          placePiece(color, x_coord, y_coord)
          empty_spaces_black -= 1
          filled_spaces_black.append(x_coord+y_coord)
          flipPieces(color, x_coord, y_coord)
          whiteTurn = True

        # error message for placing piece on filled square  
        else:
          print(Fore.RED + "Invalid move: Try again" + Fore.RESET)

      # error message for empty input
      else:
        print(Fore.RED + "Invalid move: Try again" + Fore.RESET)
  else:
    scoreBoard()  

#3 -----------------------------------------------------------------------------------------------------------
def goToBoard():
    # terminal confirmation
    print('Loading...')
    print(Fore.GREEN + "You have entered 2 Player Mode")
    print(Fore.RESET, end="")

#4 -----------------------------------------------------------------------------------------------------------
def showRules():
  start = False
  pen.up()
  pen.hideturtle()

  # TO DO: Fill in rules
  pen.setpos(-115,180)
  pen.write('''
RULES FOR OTHELLO

    DOUBLE PLAYER
''', font=(26))
  pen.setpos(-265,-150)
  pen.write('''
# There are two colours of counters - black and white

# It is an 8x8 board and they have coordinates on either axis to help place the counter.

# Starting the game:
    1)  The white counter always starts. 
    2)  The four squares in the middle of the board start with four counters already placed
          (two of each colour).
    3)  Each piece played must be laid adjacent to an opponent’s counter, such that there is a series
          of the opponent’s counter bounded by two of the player’s counters.
    4)  This can be done in three ways:
          > Horizontal
          > Vertical
          > Diagonal
    5)  When this is done, the series of the opponent’s counters flips to the colour of the current
          player’s counter.

# Ending the game:
    1)  The game ends when a player is unable to flip a counter of the opponent.
    2)  The player with the maximum number of counters at the end of the game wins!
''', font=("", 9, ""))
  while start == False:
    confirmStart = input("Enter (y) once you have read the rules: ")
    if confirmStart == "y":
      turtle.resetscreen()
      goToBoard()
      start = True

#5 -----------------------------------------------------------------------------------------------------------
def placePiece(color, x_coord, y_coord):
  def drawCircle():
    pen.down()
    pen.circle(radius=13)

  # drawing circle(white)
  pen.up()
  pen.setpos(x[x_coord], y[y_coord])
  pen.fillcolor(color)
  pen.begin_fill()
  drawCircle()
  pen.end_fill()

#6 ------------------------------------------------------------------------------------------------------------
# TO DO: Check in which direction flipping to be done
def flipPieces(color, x_coord, y_coord):
  ogY_coord = y_coord
  ogX_coord = x_coord
  coord = x_coord + y_coord
  ogCoord = coord

  def resetCoord(x_coord, y_coord, coord):
    x_coord = ogX_coord
    y_coord = ogY_coord
    coord = ogCoord

  if whiteTurn:
    toBeChecked = filled_spaces_black
  else:
    toBeChecked = filled_spaces_white

  # Vertical flipping
  resetCoord(x_coord, y_coord, coord)

  # ⬆️
  global flipN
  def flipN(y_coord):
    y_coord = str(int(y_coord) + 1)
    coord = x_coord + y_coord
    while coord in toBeChecked:
      placePiece(color, x_coord, y_coord)
      if whiteTurn:
        filled_spaces_black.remove(coord)
        filled_spaces_white.append(coord)
      else:
        filled_spaces_white.remove(coord)
        filled_spaces_black.append(coord)
      y_coord = str(int(y_coord) + 1)
      coord = x_coord + y_coord
  flipN(y_coord)

  resetCoord(x_coord, y_coord, coord)
  
  # ⬇️
  global flipS
  def flipS(y_coord):
    y_coord = str(int(y_coord) - 1)
    coord = x_coord + y_coord
    while coord in toBeChecked:
      placePiece(color, x_coord, y_coord)
      if whiteTurn:
        filled_spaces_black.remove(coord)
        filled_spaces_white.append(coord)
      else:
        filled_spaces_white.remove(coord)
        filled_spaces_black.append(coord)
      y_coord = str(int(y_coord) - 1)
      coord = x_coord + y_coord
  flipS(y_coord)
  
  # Horizontal flipping
  resetCoord(x_coord, y_coord, coord)

  # ➡️
  global flipE
  def flipE(x_coord):
    x_coord = chr(ord(x_coord) + 1)
    coord = x_coord + y_coord
    while coord in toBeChecked:
      placePiece(color, x_coord, y_coord)
      if whiteTurn:
        filled_spaces_black.remove(coord)
        filled_spaces_white.append(coord)
      else:
        filled_spaces_white.remove(coord)
        filled_spaces_black.append(coord)
      x_coord = chr(ord(x_coord) + 1)
      coord = x_coord + y_coord
  flipE(x_coord)

  resetCoord(x_coord, y_coord, coord)
  
  # ⬅️
  global flipW
  def flipW(x_coord):
    x_coord = chr(ord(x_coord) - 1)
    coord = x_coord + y_coord
    while coord in toBeChecked:
      placePiece(color, x_coord, y_coord)
      if whiteTurn:
        filled_spaces_black.remove(coord)
        filled_spaces_white.append(coord)
      else:
        filled_spaces_white.remove(coord)
        filled_spaces_black.append(coord)
      x_coord = chr(ord(x_coord) - 1)
      coord = x_coord + y_coord
  flipW(x_coord)

  # Diagonal flipping
  
  resetCoord(x_coord, y_coord, coord)
  
  # ↗️
  global flipNE
  def flipNE(x_coord, y_coord):
    y_coord = str(int(y_coord) + 1)
    x_coord = chr(ord(x_coord) + 1)
    coord = x_coord + y_coord
    while coord in toBeChecked:
      placePiece(color, x_coord, y_coord)
      if whiteTurn:
        filled_spaces_black.remove(coord)
        filled_spaces_white.append(coord)
      else:
        filled_spaces_white.remove(coord)
        filled_spaces_black.append(coord)
      y_coord = str(int(y_coord) + 1)
      x_coord = chr(ord(x_coord) + 1)
      coord = x_coord + y_coord
  flipNE(x_coord, y_coord)

  resetCoord(x_coord, y_coord, coord)

  # ↙️
  global flipSW
  def flipSW(x_coord, y_coord):
    y_coord = str(int(y_coord) - 1)
    x_coord = chr(ord(x_coord) - 1)
    coord = x_coord + y_coord
    while coord in toBeChecked:
      placePiece(color, x_coord, y_coord)
      if whiteTurn:
        filled_spaces_black.remove(coord)
        filled_spaces_white.append(coord)
      else:
        filled_spaces_white.remove(coord)
        filled_spaces_black.append(coord)
      y_coord = str(int(y_coord) - 1)
      x_coord = chr(ord(x_coord) - 1)
      coord = x_coord + y_coord
  flipSW(x_coord, y_coord)
  
  resetCoord(x_coord, y_coord, coord)
  
  # ↖️
  global flipNW
  def flipNW(x_coord, y_coord):
    y_coord = str(int(y_coord) + 1)
    x_coord = chr(ord(x_coord) - 1)
    coord = x_coord + y_coord
    while coord in toBeChecked:
      placePiece(color, x_coord, y_coord)
      if whiteTurn:
        filled_spaces_black.remove(coord)
        filled_spaces_white.append(coord)
      else:
        filled_spaces_white.remove(coord)
        filled_spaces_black.append(coord)
      y_coord = str(int(y_coord) + 1)
      x_coord = chr(ord(x_coord) - 1)
      coord = x_coord + y_coord
  flipNW(x_coord, y_coord)

  resetCoord(x_coord, y_coord, coord)
  
  # ↘️
  global flipSE
  def flipSE(x_coord, y_coord):
    y_coord = str(int(y_coord) - 1)
    x_coord = chr(ord(x_coord) + 1)
    coord = x_coord + y_coord
    while coord in toBeChecked:
      placePiece(color, x_coord, y_coord)
      if whiteTurn:
        filled_spaces_black.remove(coord)
        filled_spaces_white.append(coord)
      else:
        filled_spaces_white.remove(coord)
        filled_spaces_black.append(coord)
      y_coord = str(int(y_coord) - 1)
      x_coord = chr(ord(x_coord) + 1)
      coord = x_coord + y_coord
  flipSE(x_coord, y_coord)

#7 ------------------------------------------------------------------------------------------------------------
# TO DO: Make Scores change --> Sharvari
def scoreBoard():
  # win counter
  winsWhite = 0
  winsBlack = 0
  # drawing board
  turtle.clearscreen()
  turtle.hideturtle()
  turtle.pensize(3)
  turtle.penup()
  turtle.goto(-100,207)
  turtle.write("SCOREBOARD", font = ("", 20, ""))
  turtle.goto(-250, 150)
  turtle.showturtle()
  turtle.pendown()
  for i in range (2):
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
  turtle.setpos(-250,110)
  turtle.forward(500)
  turtle.penup()
  turtle.goto(0, 150)
  turtle.right(90)
  turtle.pendown()
  turtle.forward(200)
  turtle.hideturtle()
  turtle.speed(100)
  turtle.penup()
  turtle.goto(-150, 120)
  turtle.write("White", font = ("", 15, ""))
  turtle.goto(105, 120)
  turtle.write("Black", font = ("", 15, ""))
  turtle.goto(-150, 0)
  turtle.write(winsWhite, font = ("", 50, ""))
  turtle.goto(110, 0)
  turtle.write(winsBlack, font = ("", 50, ""))

  # Replay game
  restart = input("Play Again (y/n): ")
  turtle.clearscreen()
  if restart == "y":
    drawBoard()
  else:
    turtle.clearscreen()
    turtle.hideturtle()
    turtle.penup()
    turtle.write("Thank you for playing", font = ("", 30, ""), align = 'center')
    for i in range (5, 0, -1):
      print(Fore.RED + "Closing in", str(i) + "..." + Fore.GREEN)
      time.sleep(1)
    print("Goodbye" + Fore.RESET)
    exit()
