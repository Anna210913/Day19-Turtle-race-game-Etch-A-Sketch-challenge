from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500,height = 400)
bet = screen.textinput(title= "Place your bet", prompt= "Which turtle will win the race? Choose a colour: ")
colours =["red", "green", "purple", "blue", "yellow", "orange"]

is_race_on = False
all_turtles=[]


"""This is how i wrote my code:"""
#wayne = Turtle(shape="turtle")
#wayne.penup()
#wayne.goto(x=-230, y=-100)
#wayne.color(colours[0])
#
#arthur =Turtle(shape="turtle")
#arthur.penup()
#arthur.goto(x=-230, y=-70)
#arthur.color(colours[1])
#
#
#george =Turtle(shape="turtle")
#george.penup()
#george.goto(x=-230, y=-40)
#george.color(colours[2])
#
#chris =Turtle(shape="turtle")
#chris.penup()
#chris.goto(x=-230, y=-10)
#chris.color(colours[3])
#
#bach =Turtle(shape="turtle")
#bach.penup()
#bach.goto(x=-230, y=20)
#bach.color(colours[4])
#
#
#john =Turtle(shape="turtle")
#john.penup()
#john.goto(x=-230, y=50)
#john.color(colours[5])

"""Angela's alternative"""
y_positions =[-70, -40, -10, 20, 50, 80]


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_colour =turtle.pencolor()
            if winning_colour ==bet:
                print(f"Yay you won! the {winning_colour} turtle is the winner!")
            else:
                print(f"Womp Womp, the {winning_colour} turtle is the winner!")

        random_distance=random.randint(0,10)
        turtle.forward(random_distance)



screen.exitonclick()