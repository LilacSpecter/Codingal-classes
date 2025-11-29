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


