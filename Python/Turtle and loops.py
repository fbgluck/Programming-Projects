# Ask the user for some input
import turtle  # Library for Turtle
import math  # Library for math functions

# Create the Turtle Object
the_turtle = turtle.Turtle()
my_name = input("What is your name? ")

# Print out the message with the value that you input
print("Hello " + my_name + ". Nice to meet you.")

print("OK " + my_name + " let's have the_turtle draw a square.")


# -- Why we use loops --
# the_turtle.forward (50)
# the_turtle.left(90)
# the_turtle.forward (50)
# the_turtle.left(90)
# the_turtle.forward (50)
# the_turtle.left(90)
# the_turtle.forward (50)
# the_turtle.left(90)
# -- the same using loops is much shorter and easier to write --
# for {variable} in range (start,stop,step)
# start default = 0
# step default = 1
# -----------------------------
# for i in range(4):
#    the_turtle.forward(50)
#    the_turtle.left(90)
#    print ("the value of i is now " + str(i))
# print ("My program has completed!")

# -- different color squares --

# This is a Python list with four colors
# A list is a python data structure
# - a data structure is a fancy way of how
# - Python stores data.
# set up the colors of the sides
colorlist = ["red", "blue", "green", "orange"]

# Draw a square and calculate the length of the diag using
# Pythagorean Theorum

# Ask for the length of each side
side_length = input("What length should the side be? ")

# Convert the string input to an integer
side_length = int(side_length)

# Use the Pythagorean Theorum to calculate the diagonal
diag_length = math.sqrt((side_length**2) + (side_length**2))
print("The length of the diagonal is: " + str(diag_length))
print("Starting to draw...")
# Now draw the sides
for i in range(4):
    the_turtle.color(colorlist[i])  # pick out the next color
    the_turtle.forward(side_length)  # draw the side
    the_turtle.left(90)  # and position for the next side
#    print("side " + str(i) + " is " + colorlist[i])
# Now, draw the diagonal
the_turtle.left(45)
the_turtle.forward(diag_length)
# And move the turtle out of the way
the_turtle.penup()
the_turtle.setpos(-20, 0)
# Do a little Dance !!
the_turtle.left(180)
the_turtle.right(180)
input("ENTER to finish and close program")
