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

#import turtle

#turtle.Screen().bgcolor("teal")

#sc= turtle.Screen()
#sc.setup(400,400)

#turtle.title("Welcome to Turtle Window")

#board = turtle.Turtle()

#for i in range(4):
#    board.forward(100)
#    board.right(90)
#    i= i+1

#Activity 2///

#import turtle
#turtle.Screen().bgcolor("white")
#board = turtle.Turtle()

#board.forward(100) # draw base

#board.left(120)
#board.forward(100)

#board.left(120)
#board.forward(100)

#board.penup()
#board.right(150)
#board.forward(50)

#board.pendown()
#board.right(90)
#board.forward(100)

#board.right(120)
#board.forward(100)

#board.right(120)
#board.forward(100)

#turtle.done()

#Activity 3///

import turtle
t = turtle.Turtle()
s = turtle.Screen()
colors = ['red','purple','blue','green','orange','yellow']
s.bgcolor('white')
t.speed('fastest')
t.hideturtle()
while True:
    for x in range(200):
        t.pencolor(colors[x%len(colors)])
        t.width(x/100 + 1)
        t.forward(x)
        t.left(59)
    t.right(239)
    for x in range(200, 0, -1):
        t.pencolor('black')
        t.width(x/100 + 7)
        t.forward(x)
        t.right(59)