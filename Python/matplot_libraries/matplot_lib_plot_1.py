# Sample plots using MatPlotLib
# This helped a lot: https://juejung.github.io/jdocs/Comp/html/Slides_Plot.html
import numpy as np
from matplotlib import pyplot as plt
# Generate a list of values for x
# original function:
# ((y-1)**2 / 9)- ((x+1)**2 / 16) =1
# I had to solve this function for y
#
# Set up range of values for x
# x is an element of the list each time we iterate
# Option 1 to generate a range of numbers for x
# x_values = np.array (list(range(-100,100,5)))
# Option 2 to generate a range of numbers for x
# see this page: https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
# numpy.linspace(start, stop, num=50, endpoint=True,
#               retstep=False, dtype=None, axis=0)
x_values = np.linspace(-100, 100, 101)
# Option 3 to generate a range of numbers for x
# x_values = np.array([0, 1, 2, 3, 4])

# Set up the graph
plt.title("Function Plot")  # Caption for the title
plt.xlabel("x axis caption")  # Caption for the X Axis
plt.ylabel("y axis caption")  # Caption for the Y Axis
plt.grid(True)  # Show a grid on the graph

# And actually do the plot
for x in range(len(x_values)):  # iterate for each value of x
    # Use the math library to calculate the square root
    # y=(math.sqrt((1+(((x_values[x]+1)**2)/16))*9)+1)

    # Use the numpy library to calculate sqrt
    # y = (np.sqrt((1+(((x_values[x]+1)**2)/16))*9)+1)
    y = ((x_values[x])**3)-((5*(x_values[x]))**2)+(7*(x_values[x]))-5
    # y = -(((x_values[x]))**3) - (3*((x_values[x]))**2) - 1
    # y = ((x_values[x])**4) - (2*((x_values[x]))**2) + 3
    # y = ((x_values[x])**4) - ((x_values[x])**2)
    # y = -(2/(((x_values[x]))**2)-4)
    # y = ((2*((x_values[x]))-8)**(2/3))

    #

    print(f'x= {x_values[x]} and y= {y}')
    plt.plot(x_values[x], y,  # This actually creates the plot
             color='green',
             linestyle='solid',
             linewidth=1,
             marker='o',
             markerfacecolor='green',
             markersize=1
             )
# Then display the plot that was built
plt.show()  # Because nothing happens if you don't do this
