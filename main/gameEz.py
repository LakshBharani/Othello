# easy version of Othello

import turtle
print("You have entered easy mode")
sc = turtle.Screen()
   
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
       
# turtle speed
pen.speed(100)
       
# loops for board
for i in range(8):

  pen.up()
       
# position for row
  pen.setpos(-170, -130 + 40 * i)
       
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
       
    # hide the turtle
pen.hideturtle()
turtle.done()