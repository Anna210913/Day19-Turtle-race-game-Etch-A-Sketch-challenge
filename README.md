# Day19-Turtle-race-game-Etch-A-Sketch Challenge

For Day 19 we built a super fun **Turtle Race Game** using Python’s Turtle graphics module. This was such a cool project because it made me feellike a game programmer.
You (the user) gets a pop-up window asking you which turtle color you think will win, then the race begins.
You place your bet and watch the colorful turtles move across the screen to the finish line. (the winner is completely randomised)

We also did a fun bonus challenge: an **Etch-A-Sketch** drawing program where you control a turtle with your keyboard arrows to draw.  
(PS: I uploaded this challenge code in the files area too so you can try it out)

# What we learned:

- Higher Order functions and event listeners: python can take functions as inputs to other functions ( this is **Higher order functions**)
- Object State and Instances :Each turtle has a **state** (like its position) that changes as the race happens.
**Instances** of a class allows each turtle in the race to be its own object, with its own colour and starting point.
- Turtle coordinates system

# How the code works:
'screen = Screen()' — creates the game window where the race happens

'screen.setup(width=500, height=400)' — sets the window size 

'screen.textinput(title, prompt)' — pops up a window asking the user to bet on a turtle color

'Turtle(shape="turtle")' — creates a turtle racer (each one is an object instance)

'turtle.color("red")' — gives that turtle its unique racing color

'turtle.penup()' — lifts the pen so the turtle moves without drawing lines at the start

'turtle.goto(x, y)' — positions each turtle on the starting line in different lanes

'all_turtles.append(new_turtle)' — stores each turtle inside a list so we can manage them in a loop

'if bet:' — checks if the user placed a bet; if yes, the race begins

'while is_race_on:' — keeps the race running until a winner is found

'random.randint(0, 10)' — generates a random movement, making the race unpredictable and fun

'turtle.forward(random_distance)' — moves the turtle forward by the random number

'turtle.xcor()' — checks the turtle’s x-position to see if it crossed the finish line

'turtle.pencolor()' — reads the winning turtle’s color to compare with the user’s bet

'print(...)' — prints whether the player won or lost

'screen.exitonclick()' — keeps the window open until clicked so the user can view results
