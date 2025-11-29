#import turtle
#creating canvas
#turtle.Screen().bgcolor("teal")
#turtle.Screen().setup(400, 400)
#turtle object creation
#polygon = turtle.Turtle()
#num_sides = 6
#side_length = 10
#angle = 360.0 / num_sides
#creating a square
#for i in range(num_sides):
#    polygon.forward(side_length)
#    polygon.right(angle)
#turtle.done()

#Activity 1\\\

import turtle

turtle.Screen().bgcolor("teal")

sc= turtle.Screen()
sc.setup(400,400)

turtle.title("Welcome to Turtle Window")

board = turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.right(90)
    i= i+1

#Activity 2///

import turtle
turtle.Screen().bgcolor("white")
board = turtle.Turtle()

board.forward(100) # draw base

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

turtle.done()

