import turtle

# Create the turtle object
t = turtle.Turtle()
t.speed(3) # 1 is slowest, 10 is fast, 0 is instant

# --- Draw a Square ---
# A square has 4 equal sides and 90-degree angles
for _ in range(4):
    t.forward(100) # Move forward 100 pixels
    t.left(90)     # Turn left 90 degrees

# --- Move to a new position ---
t.penup()      # Lift the pen so it stops drawing
t.goto(150, 0) # Move to the right (x=150, y=0)
t.pendown()    # Put the pen back down to draw again

# --- Draw a Circle ---
# The number inside the parentheses is the radius (50 pixels)
t.circle(50)

# Keep the window open until you click it away
turtle.done()