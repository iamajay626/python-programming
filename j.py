from turtle import *

# S
bgcolor('black')

# Define the positions to draw the "J"
pos = [(0, -40), (0, 40)]  # Adjusted positions

# Loop through the positions to draw the shapes
for x, y in pos:
    up()
    goto(x, y)
    down()
    fillcolor('blue')  # Set the fill color to blue
    begin_fill()
    for _ in range(2):
        forward(200)
        left(90)
        forward(40)
        left(90)
    end_fill()

# Move to a specific position to draw the curved part of the "J"
up()
goto(0, -40)  # Adjusted position
down()

# Set the fill color to green
fillcolor('green')
begin_fill()

# Draw the curved part of the "J"
left(112)  # Adjusted angle
for _ in range(2):
    forward(217)
    left(68)
    forward(40)
    left(112)

end_fill()

# End the drawing
done()