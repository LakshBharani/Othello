# 1 player mode (Player vs Computer)

import turtle

# coordinates of pieces
global x
x = {"a":-145, "b":-105, "c":-65, "d":-25, "e":15, "f":55, "g":95, "h":135}
global y
y = {"1":-124, "2": -84, "3":-44, "4":-4, "5":36, "6":76, "7":116, "8":156}

#1 -----------------------------------------------------------------------------------------------------------
def drawBoard():
  empty_spaces_white = 30
  empty_spaces_black = 30

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

  # placing more pieces
  while empty_spaces_white != 0:
    coord = input("Enter coordinates: ")
    global x_coord
    x_coord = coord[0]
    global y_coord
    y_coord = coord[1]
    empty_spaces_white -= 1
    playerMove_white()
  else:
    print("No more moves left")

  # End editing board
  sc.update()
  turtle.mainloop()

#2 -----------------------------------------------------------------------------------------------------------
def singlePlayer():
    # terminal confirmation
    print("You have entered Single Player Mode")
    drawBoard()

#3 -----------------------------------------------------------------------------------------------------------
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