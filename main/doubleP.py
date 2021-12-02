# 2 player mode (Player vs Computer)

import turtle
from colorama import Fore

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

  filled_spaces_white = ["d4", "e5"]
  filled_spaces_black = ["d5", "e4"]

  while empty_spaces_white != 0 or empty_spaces_black != 0:
    global x_coord
    global y_coord
    global whiteTurn

    # White player's turn
    if whiteTurn == True:
      print(Fore.YELLOW + "------- White -------" + Fore.RESET)
      coord = input("Enter coordinates: " + Fore.YELLOW)
      print(Fore.RESET, end="")
      if len(coord) != 0:
        x_coord = coord[0]
        y_coord = coord[1:]

        if (x_coord+y_coord) not in filled_spaces_white and (x_coord+y_coord) not in filled_spaces_black and x_coord in x.keys() and y_coord in y.keys():
          playerMove_white()
          empty_spaces_white -= 1
          filled_spaces_white.append(x_coord+y_coord)
          whiteTurn = False

        # error message for placing piece on filled square  
        else:
          print(Fore.RED + "Invalid move: Try again" + Fore.RESET)

      # error message for empty input
      else:
        print(Fore.RED + "Invalid move: Try again" + Fore.RESET)

      # Black player's turn
    else:
      print(Fore.BLUE + "------- Black -------" + Fore.RESET)
      coord = input("Enter coordinates: " + Fore.BLUE)
      print(Fore.RESET, end="")
      if len(coord) != 0:
        x_coord = coord[0]
        y_coord = coord[1:]
        if (x_coord+y_coord) not in filled_spaces_black and (x_coord+y_coord) not in filled_spaces_white and x_coord in x.keys() and y_coord in y.keys():
          playerMove_black()
          empty_spaces_black -= 1
          filled_spaces_black.append(x_coord+y_coord)
          whiteTurn = True

        # error message for placing piece on filled square  
        else:
          print(Fore.RED + "Invalid move: Try again" + Fore.RESET)

      # error message for empty input
      else:
        print(Fore.RED + "Invalid move: Try again" + Fore.RESET)
#3 -----------------------------------------------------------------------------------------------------------
def goToBoard():
    # terminal confirmation
    print('Loading...')
    print(Fore.GREEN + "You have entered 2 Player Mode")
    print(Fore.RESET, end="")

#4 -----------------------------------------------------------------------------------------------------------
def showRules():
  start = False
  while start == False:
    pen.up()
    pen.setpos(-165,100)

    # TO DO: Fill in rules
    pen.write("")
    pen.hideturtle()
    confirmStart = input("Enter (y) once you have read the rules: ")
    if confirmStart == "y":
      goToBoard()
      start = True


#5 -----------------------------------------------------------------------------------------------------------
def playerMove_white():
  def drawCircle():
    pen.down()
    pen.circle(radius=13)

  # drawing circle(white)
  col = "white"
  pen.up()
  pen.setpos(x[x_coord], y[y_coord])
  pen.fillcolor(col)
  pen.begin_fill()
  drawCircle()
  pen.end_fill()

def playerMove_black():
  def drawCircle():
    pen.down()
    pen.circle(radius=13)

  # drawing circle(white)
  col = "black"
  pen.up()
  pen.setpos(x[x_coord], y[y_coord])
  pen.fillcolor(col)
  pen.begin_fill()
  drawCircle()
  pen.end_fill()
