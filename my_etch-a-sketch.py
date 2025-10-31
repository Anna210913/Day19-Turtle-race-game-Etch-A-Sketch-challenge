from turtle import Turtle, Screen

wayne = Turtle()
screen = Screen()

def move():
    wayne.forward(10)

def move_back():
    wayne.back(10)

def clockwise():
    wayne.right(10)

def anti_clockwise():
    wayne.left(10)

def erase():
    wayne.clear()


screen.listen()

screen.onkey(key = "W", fun= move)
screen.onkey(key="B", fun=move_back)
screen.onkey(key="A", fun=clockwise)
screen.onkey(key="D", fun=anti_clockwise)
screen.onkey(key="C", fun=erase)

screen.exitonclick()