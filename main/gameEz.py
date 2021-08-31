# easy version of Othello

import turtle

# coordinates of pieces
x = [a,b,c,d,e,f,g,h] = [-145,-105,-65,-25,15,55,95,135]
y = [0,-124,-84,-44,-4,36,76,116,156]

print("You have entered Easy mode")

# method to draw board
def drawBoard():
  sc = turtle.Screen()
  sc.tracer(3)

  # create turtle
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

     # ready to draw
    pen.down()

  # row
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
    pen.setpos(xtemp,200)
    pen.write(chr(i+64))
    xtemp+=40

  def drawCircle():
    pen.down()
    pen.circle(radius=13)

  # drawing init circle(white)
  col = "white"
  pen.up()
  pen.setpos(e,y[5])
  pen.fillcolor(col)
  pen.begin_fill()
  drawCircle()
  pen.end_fill()

  pen.up()
  pen.setpos(d,y[4])
  pen.fillcolor(col)
  pen.begin_fill()
  drawCircle()
  pen.end_fill()

  # drawing init circle(black)
  col = "black"
  pen.up()
  pen.setpos(d,y[5])
  pen.fillcolor(col)
  pen.begin_fill()
  drawCircle()
  pen.end_fill()

  pen.up()
  pen.setpos(e,y[4])
  pen.fillcolor(col)
  pen.begin_fill()
  drawCircle()
  pen.end_fill()

  # hide the turtle
  pen.hideturtle()
  sc.update()
  turtle.done()
drawBoard()
