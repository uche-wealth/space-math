import turtle

pen = turtle.Turtle()


def move_pen(x, y):
    """Move turtle to specified location"""
    pen.pu()
    pen.goto(x, y)
    pen.pd()

def first_star(line=50):
    """Draw first star"""
    pen.begin_fill()
    for _ in range(3):
        pen.fd(line)
        pen.lt(120)
    pen.end_fill()

def second_star(line=50):
    """Draw second star"""
    pen.begin_fill()
    for _ in range(3):
        pen.fd(line)
        pen.rt(120)
    pen.end_fill()

def star_pen_attrs():
    """Set attributes for pen drawing stars"""
    pen.color('white')
    pen.ht()
    pen.speed(0)


def draw_left_stars():
    """Draw stars on the Left side."""
    star_pen_attrs()
    move_pen(-350, 0)
    first_star()
    move_pen(-350, 30)
    second_star()
    move_pen(-350, -200)
    first_star()
    move_pen(-350, -170)
    second_star()
    move_pen(-350, 200)
    first_star()
    move_pen(-350, 230)
    second_star()

def draw_right_stars():
    """Draw stars on the Right side"""
    star_pen_attrs()
    move_pen(350, 0)
    first_star()
    move_pen(350, 30)
    second_star()
    move_pen(350, -200)
    first_star()
    move_pen(350, -170)
    second_star()
    move_pen(350, 200)
    first_star()
    move_pen(350, 230)
    second_star()

