# 1 player mode (Player vs Bot - Hard)

import turtle
from typing import final
from colorama import Fore
import time, random

global whiteTurn
whiteTurn = True

# coordinates of pieces
global x
x = {"a":-145, "b":-105, "c":-65, "d":-25, "e":15, "f":55, "g":95, "h":135}
global y
y = {"1":-124, "2": -84, "3":-44, "4":-4, "5":36, "6":76, "7":116, "8":156}

# win counter
global winsWhite
winsWhite = 0
global winsBlack
winsBlack = 0

#1 -----------------------------------------------------------------------------------------------------------
def drawBoard():
  sc = turtle.Screen()
  sc.tracer(3)

  # create turtle
  global pen
  pen = turtle.Turtle()
  sc.title("Othello --> Single Player")

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

  # Board heading
  pen.up()
  pen.goto(0, 210)
  pen.write("Othello", font=("", 50, ""), align="center")

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

  # drawing init circle(white)
  placePiece(color="white", x_coord="e", y_coord="5")
  placePiece(color="white", x_coord="d", y_coord="4")

  # drawing init circle(black)
  placePiece(color="black", x_coord="d", y_coord="5")
  placePiece(color="black", x_coord="e", y_coord="4")

  # initial 4 pieces
  global filled_spaces_white
  filled_spaces_white = ["d4", "e5"]
  global filled_spaces_black
  filled_spaces_black = ["d5", "e4"]

  # drawing live score table
  liveScore(drawTable=True)

  # Placing more pieces
  startGame()

  # End editing board
  sc.update()
  turtle.mainloop()

#2 -----------------------------------------------------------------------------------------------------------
def startGame():
  empty_spaces_white = 30
  empty_spaces_black = 30

  while empty_spaces_white != 0 or empty_spaces_black != 0:
    global x_coord
    global y_coord
    global whiteTurn

    # White player's turn
    if whiteTurn == True:
      highlightActivePlayer()
      color = "white"
      print(Fore.YELLOW + "------- White -------" + Fore.RESET + "\n" "Enter coordinates: " + Fore.YELLOW, end = "")
      decideBotMove(color)
      coord = input(Fore.YELLOW)
      print(Fore.RESET, end="")
      # pass turn
      # if coord == "p" or coord == "P":
      #   whiteTurn = False
      #   continue
      if len(coord) != 0:
        x_coord = coord[0].casefold()
        y_coord = coord[1:].casefold()

        if (x_coord+y_coord) not in filled_spaces_white and (x_coord+y_coord) not in filled_spaces_black and x_coord in x.keys() and y_coord in y.keys():
          checkDirection(color, x_coord, y_coord)
          if isReadyToPlace == True:
            placePiece(color, x_coord, y_coord)
            empty_spaces_white -= 1
            filled_spaces_white.append(x_coord+y_coord)
            flipPieces(color, x_coord, y_coord)
            liveScore(drawTable=False)
            whiteTurn = False
          else:
            print(Fore.RED + "Invalid move: Try again" + Fore.RESET)

        # error message for placing piece on filled square  
        else:
          print(Fore.RED + "Invalid move: Try again" + Fore.RESET)

      # error message for empty input
      else:
        print(Fore.RED + "Invalid move: Try again" + Fore.RESET)

      # Black player's turn
    else:
      highlightActivePlayer()
      color = "black"
      print(Fore.BLUE + "------- Black -------" + Fore.RESET + "\n" "Enter coordinates: " + Fore.BLUE, end = "")
      decideBotMove(color)
      time.sleep(3)
      print(finalBotCoord)
      print(Fore.RESET, end="")
      
      x_coord = finalBotCoord[0].casefold()
      y_coord = finalBotCoord[1:].casefold()
      placePiece(color, x_coord, y_coord)
      empty_spaces_black -= 1
      filled_spaces_black.append(finalBotCoord)
      checkDirection(color, x_coord, y_coord)
      flipPieces(color, x_coord, y_coord)
      liveScore(drawTable=False)
      whiteTurn = True
     
  else:
    endGame() 

#3 -----------------------------------------------------------------------------------------------------------
def goToBoard():
    # terminal confirmation
    print('Loading...')
    print(Fore.GREEN + "You have entered 1 Player Mode")
    print(Fore.RESET, end="")

#4 -----------------------------------------------------------------------------------------------------------
def showRules():
  start = False
  pen.up()
  pen.hideturtle()
  pen.setpos(-115,180)
  pen.write('''
RULES FOR OTHELLO

    SINGLE PLAYER
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
  pen.hideturtle()
  pen.up()
  pen.setpos(x[x_coord], y[y_coord])
  pen.fillcolor(color)
  pen.begin_fill()
  drawCircle()
  pen.end_fill()

#6 ------------------------------------------------------------------------------------------------------------
def flipPieces(color, x_coord, y_coord):
  ogY_coord = y_coord
  ogX_coord = x_coord

  if whiteTurn:
    toBeChecked = filled_spaces_black
  else:
    toBeChecked = filled_spaces_white

  # Vertical flipping

  # ⬆️
  global flipN
  def flipN(y_coord):
    y_coord = str(int(ogY_coord) + 1)
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
  if inN == True:
    flipN(y_coord)
  
  # ⬇️
  global flipS
  def flipS(y_coord):
    y_coord = str(int(ogY_coord) - 1)
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
  if inS == True:
    flipS(y_coord)
  
  # Horizontal flipping
  # ➡️
  global flipE
  def flipE(x_coord):
    x_coord = chr(ord(ogX_coord) + 1)
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
  if inE == True:
    flipE(x_coord)
  
  # ⬅️
  global flipW
  def flipW(x_coord):
    x_coord = chr(ord(ogX_coord) - 1)
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
  if inW == True:
    flipW(x_coord)

  # Diagonal flipping  
  # ↗️
  global flipNE
  def flipNE(x_coord, y_coord):
    y_coord = str(int(ogY_coord) + 1)
    x_coord = chr(ord(ogX_coord) + 1)
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
  if inNE == True:
    flipNE(x_coord, y_coord)

  # ↙️
  global flipSW
  def flipSW(x_coord, y_coord):
    y_coord = str(int(ogY_coord) - 1)
    x_coord = chr(ord(ogX_coord) - 1)
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
  if inSW == True:
    flipSW(x_coord, y_coord)
  
  # ↖️
  global flipNW
  def flipNW(x_coord, y_coord):
    y_coord = str(int(ogY_coord) + 1)
    x_coord = chr(ord(ogX_coord) - 1)
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
  if inNW == True:
    flipNW(x_coord, y_coord)
  
  # ↘️
  global flipSE
  def flipSE(x_coord, y_coord):
    y_coord = str(int(ogY_coord) - 1)
    x_coord = chr(ord(ogX_coord) + 1)
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
  if inSE == True:
    flipSE(x_coord, y_coord)

#7 ------------------------------------------------------------------------------------------------------------
# Keeps track of white and black pieces on the board currently
def liveScore(drawTable):
  # draws table only once along with the board
  if drawTable == True:
    turtle.penup()
    turtle.goto(-150, -175)
    turtle.pendown()
    for i in range (2):
      turtle.forward(300)
      turtle.right(90)
      turtle.forward(100)
      turtle.right(90)
    turtle.penup()
    turtle.goto(-150,-200)
    turtle.pendown()
    turtle.forward(300)
    turtle.penup()
    turtle.goto(0, -175)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(100)
    turtle.penup()
    turtle.hideturtle() 
    turtle.goto(-75 ,-197)
    turtle.write("White", font=("", 12, ""), align="center")
    turtle.goto(75 ,-197)
    turtle.write("Black", font=("", 12, ""), align="center")
  def mask(x, y):
    turtle.setpos(x, y)
    for i in range(2):
      turtle.fillcolor("lightblue")
      turtle.begin_fill()
      turtle.forward(72)
      turtle.right(90)
      turtle.forward(147)
      turtle.right(90)
      turtle.end_fill()

  # shows whose turn it is
  global highlightActivePlayer 
  def highlightActivePlayer():
    def currentPlayerMask(x, y, color):
      turtle.setpos(x, y)
      for i in range(2):
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.forward(22)
        turtle.right(90)
        turtle.forward(147)
        turtle.right(90)
        turtle.end_fill()
  
    if whiteTurn == True:
      currentPlayerMask(-1, -177, "yellow")
      turtle.goto(-75 ,-197)
      turtle.write("White", font=("", 12, ""), align="center")
      currentPlayerMask(149, -177, "white")
      turtle.goto(75 ,-197)
      turtle.write("Black", font=("", 12, ""), align="center")
    elif whiteTurn == False:
      currentPlayerMask(149, -177, "yellow")
      turtle.goto(75 ,-197)
      turtle.write("Black", font=("", 12, ""), align="center")
      currentPlayerMask(-1, -177, "white")
      turtle.goto(-75 ,-197)
      turtle.write("White", font=("", 12, ""), align="center")

  mask(-1, -202)
  turtle.setpos(-75, -265)
  turtle.write(len(filled_spaces_white), font=("", 36, ""), align="center")

  mask(149, -202)
  turtle.setpos(75, -265)
  turtle.write(len(filled_spaces_black), font=("", 36, ""), align="center")

#8 ------------------------------------------------------------------------------------------------------------
# Keeps track of rounds won by each player
def scoreBoard():
  # drawing board
  global winsWhite
  global winsBlack
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
  # updating wins based on number of pieces of each color at end of the game
  if filled_spaces_white > filled_spaces_black:
    winsWhite += 1
  elif filled_spaces_black > filled_spaces_white:
    winsBlack += 1
  elif filled_spaces_white == filled_spaces_black:
    winsBlack += 1
    winsWhite += 1
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

#9 ------------------------------------------------------------------------------------------------------------
def checkDirection(color, x_coord, y_coord):
  global isReadyToPlace
  isReadyToPlace = False
  
  # booleans to keep track of direction
  global inN, inS, inE, inW,inNE, inNW, inSE, inSW
  inN = False
  inS = False
  inE = False
  inW = False
  inNE = False
  inSE = False
  inSW = False
  inNW = False

  # count num of pieces flipped by bot on every sqaure
  global piecesFlipped
  piecesFlipped = 0

  # initial coords
  ogY_coord = y_coord
  ogX_coord = x_coord

  if color == "white":
    toBeChecked = filled_spaces_black
    endPiece = filled_spaces_white
  elif color == "black":
    toBeChecked = filled_spaces_white
    endPiece = filled_spaces_black

  # checking in N
  counter = 0
  y_coord = str(int(ogY_coord) + 1)
  while (ogX_coord + str(int(ogY_coord) + 1)) in toBeChecked and y_coord in y:
    y_coord = str(int(y_coord) + 1)
    coord = x_coord+y_coord
    counter += 1
    if coord in endPiece:
      inN = True
      isReadyToPlace = True
      piecesFlipped += counter
      break
    elif coord not in toBeChecked:
      break

  # checking in S
  counter = 0
  y_coord = str(int(ogY_coord) - 1)
  while (ogX_coord + str(int(ogY_coord) - 1)) in toBeChecked and y_coord in y:
    y_coord = str(int(y_coord)-1)
    coord = x_coord+y_coord
    counter += 1
    if coord in endPiece:
      inS = True
      isReadyToPlace = True
      piecesFlipped += counter
      break
    elif coord not in toBeChecked:
      break

  # checking in E
  counter = 0
  x_coord = chr(ord(ogX_coord) + 1)
  while (chr(ord(ogX_coord) + 1) + ogY_coord) in toBeChecked and x_coord in x:
    x_coord = chr(ord(x_coord) + 1)
    coord = x_coord + ogY_coord
    counter += 1
    if coord in endPiece:
      inE = True
      isReadyToPlace = True
      piecesFlipped += counter
      break
    elif coord not in toBeChecked:
      break

  # checking in W
  counter = 0
  x_coord = chr(ord(ogX_coord) - 1)
  while (chr(ord(ogX_coord) - 1) + ogY_coord) in toBeChecked and x_coord in x:
    x_coord = chr(ord(x_coord) - 1)
    coord = x_coord + ogY_coord
    counter += 1
    if coord in endPiece:
      inW = True
      isReadyToPlace = True
      piecesFlipped += counter
      break
    elif coord not in toBeChecked:
      break

  # checking in NE
  counter = 0
  x_coord = chr(ord(ogX_coord) + 1)
  y_coord = str(int(ogY_coord) + 1)
  while (chr(ord(ogX_coord) + 1) + str(int(ogY_coord) + 1)) in toBeChecked and y_coord in y and x_coord in x:
    x_coord = chr(ord(x_coord) + 1)
    y_coord = str(int(y_coord) + 1)
    coord = x_coord+y_coord
    counter += 1
    if coord in endPiece:
      inNE = True
      isReadyToPlace = True
      piecesFlipped += counter
      break
    elif coord not in toBeChecked:
      break

  # checking in SE
  counter = 0
  x_coord = chr(ord(ogX_coord) + 1)
  y_coord = str(int(ogY_coord) - 1)
  while (chr(ord(ogX_coord) + 1) + str(int(ogY_coord) - 1)) in toBeChecked and y_coord in y and x_coord in x:
    x_coord = chr(ord(x_coord) + 1)
    y_coord = str(int(y_coord) - 1)
    coord = x_coord + y_coord
    counter += 1
    if coord in endPiece:
      inSE = True
      isReadyToPlace = True
      piecesFlipped += counter
      break
    elif coord not in toBeChecked:
      break

  # checking in NW
  counter = 0
  x_coord = chr(ord(ogX_coord) - 1)
  y_coord = str(int(ogY_coord) + 1)
  while (chr(ord(ogX_coord) - 1) + str(int(ogY_coord) + 1)) in toBeChecked and y_coord in y and x_coord in x:
    x_coord = chr(ord(x_coord) - 1)
    y_coord = str(int(y_coord) + 1)
    coord = x_coord+y_coord
    counter += 1
    if coord in endPiece:
      inNW = True
      isReadyToPlace = True
      piecesFlipped += counter
      break
    elif coord not in toBeChecked:
      break

  # checking in SW
  counter = 0
  x_coord = chr(ord(ogX_coord) - 1)
  y_coord = str(int(ogY_coord) - 1)
  while (chr(ord(ogX_coord) - 1) + str(int(ogY_coord) - 1)) in toBeChecked and y_coord in y and x_coord in x:
    x_coord = chr(ord(x_coord) - 1)
    y_coord = str(int(y_coord) - 1)
    coord = x_coord+y_coord
    counter += 1
    if coord in endPiece:
      inSW = True
      isReadyToPlace = True
      piecesFlipped += counter
      break
    elif coord not in toBeChecked:
      break

#10 ------------------------------------------------------------------------------------------------------------
def decideBotMove(color):
  global finalBotCoord
  finalBotCoord = ""
  tempPiecesFlipped = 0
  # list with all coords which flip max pieces
  liCoords = []

  # check on which coords max pieces will flip (hard difficulty bot)
  for x_coord in x:
    for y_coord in y:
      tempCoord = x_coord + y_coord
      if tempCoord not in filled_spaces_black and tempCoord not in filled_spaces_white:
        checkDirection(color, x_coord, y_coord)
        if isReadyToPlace == True:
          if piecesFlipped >= tempPiecesFlipped:
            tempPiecesFlipped = piecesFlipped
  # creates a list of all coords which flip the same num of max pieces          
  for x_coord in x:
    for y_coord in y:
      tempCoord = x_coord + y_coord
      if tempCoord not in filled_spaces_black and tempCoord not in filled_spaces_white:
        checkDirection(color, x_coord, y_coord)
        if isReadyToPlace == True:
          if piecesFlipped == tempPiecesFlipped:
            liCoords.append(tempCoord)
  if len(liCoords) != 0:
    finalBotCoord = random.choice(liCoords)
  else:
    if whiteTurn == True:
      print(Fore.YELLOW + "No possible moves found")
    else:
      print(Fore.BLUE + "No possible moves found")
    endGame()

#11 ------------------------------------------------------------------------------------------------------------
def endGame():
    for i in range (5, 0, -1):
      print(Fore.RED + "Loading scoreboard", str(i) + "..." + Fore.GREEN)
      time.sleep(1)
    print("Game Over" + Fore.RESET)
    scoreBoard()