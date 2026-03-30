import turtle

pen = turtle.Turtle()


def move_pen(x, y):
    """Move turtle to specified location"""
    pen.pu()
    pen.goto(x, y)
    pen.pd()
