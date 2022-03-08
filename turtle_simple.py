import turtle
import math

# This file contains a simple implementation of the shapes we discussed in class.
# No effort has been made to remove duplication or to refactor the functionality:
# Every function works by itself.


def draw_square(t, length):
    """
    Draw a square with a turtle. Arguments:
        t - A Turtle object
        length - the length of each side of the square.
    """
    for i in range(4):
        t.forward(length)
        t.left(90)


def draw_polygon(t, num_sides, length):
    """
    Draw a polygon with a turtle. Arguments:
        t - A Turtle object
        num_sides - The number of sides the polygon should have
        length - The length of each side
    """
    for i in range(num_sides):
        t.forward(length)
        t.left(360 / num_sides)


def draw_circle(t, r):
    """
    Draw a circle with a turtle. Arguments:
        t - A Turtle object
        r - The radius of the circle
    """
    circumference = 2 * math.pi * r

    # Calculate the number of sides. The number of sides is calculated as a
    # fraction of the circumference: the number of sides is approximately 1/3
    # of the circumference. Experiment with the denominator constant to see how
    # it affects she shape.
    num_sides = int(circumference / 3) + 1
    length = circumference / num_sides

    for i in range(num_sides):
        t.forward(length)
        t.left(360 / num_sides)


def draw_arc(t, r, angle):
    """
    Draw an open arc. An arc is a portion of a circle, and may be
    open or closed. Arguments:
        t - A Turtle object
        r - The radius of the arc
        angle - Degrees of the arc.
    """

    # Determine the length of the arc as a fraction of a circle (360 degrees)
    arc_length = 2 * math.pi * r * angle / 360

    # Calculate the number of sides. The number of sides is calculated as a
    # fraction of the arc length: the number of sides is approximately 1/3
    # of the arc length. Experiment with the denominator constant to see how
    # it affects she shape.
    num_sides = int(arc_length / 3) + 1
    length = arc_length / num_sides

    for i in range(num_sides):
        t.forward(length)
        t.left(angle / num_sides)


def draw_polyline(t, n, length, angle):
    """
    Draw an open polyline. A polyline is composed of multiple line segments
    at a fixed angle. The polyline may be open or closed.
        t - A Turtle object
        n - The number of sides
        length - The length of each side
        angle - The angle between sides
    """
    for i in range(n):
        t.forward(length)
        t.left(angle)


t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.up()
t1.forward(100)
t1.down()
draw_circle(t1, 30)
draw_square(t1, 50)
draw_arc(t1, 80, 190)

t2.up()
t2.left(180)
t2.forward(100)
t2.down()
draw_polygon(t2, 3, 150)
draw_polyline(t2, 3, 50, 100)


turtle.mainloop()
