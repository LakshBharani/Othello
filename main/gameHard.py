# hard version of Othello

import turtle

xCord = [a,b,c,d,e,f,g,h]= [0,0,0,-25,14,0,0,0]
yCord = [0,0,0,0,-4,37,0,0,0]

print("You have entered Hard mode")
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

def drawCircle():
  pen.down()
  pen.circle(radius=13)

# drawing init circle(white)
col = "white"
pen.up()
pen.setpos(e,yCord[5])
pen.fillcolor(col)
pen.begin_fill()
drawCircle()
pen.end_fill()

pen.up()
pen.setpos(d,yCord[4])
pen.fillcolor(col)
pen.begin_fill()
drawCircle()
pen.end_fill()

# drawing init circle(black)
col = "black"
pen.up()
pen.setpos(d,yCord[5])
pen.fillcolor(col)
pen.begin_fill()
drawCircle()
pen.end_fill()

pen.up()
pen.setpos(e,yCord[4])
pen.fillcolor(col)
pen.begin_fill()
drawCircle()
pen.end_fill()

# hide the turtle
pen.hideturtle()
sc.update()
turtle.done()