import turtle

turtlex = 0
turtley = 0

def turtle_moveup():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def turtle_movedown():
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.stamp()

def turtle_moveright():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def turtle_moveleft():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def turtle_reset():
    turtle.reset()

turtle.shape("turtle")
turtle.onkey(turtle_moveup, 'w')
turtle.onkey(turtle_movedown, 's')
turtle.onkey(turtle_moveright, 'd')
turtle.onkey(turtle_moveleft, 'a')
turtle.onkey(turtle_reset, "Escape")
turtle.listen()

