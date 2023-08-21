from turtle import *

# Set the speed
speed(0)

# Set up the screen
bgcolor("black")

# Create a turtle
star_turtle = Turtle()

# Customize the turtle's appearance
color("blue")

# Hide the turtle
hideturtle()

# Move the turtle to the starting position
penup()
goto(-150, 0)
pendown()

# Draw the star
for _ in range(9):
    forward(250)
    right(160)
    color("red")  # Customize for the lines appearance
    for _ in range(6):
        forward(150)
        right(160)
        color("lightgreen")
        for _ in range(4):
            forward(100)
            color("blue")
            right(160)

# Close the turtle graphics window when clicked
exitonclick()