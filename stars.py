import turtle


class DrawStars:
    """Draw Stars"""
    def __init__(self):
        self.pen = turtle.Turtle()

    def __move_pen(self, x, y):
        """Move turtle to specified location"""
        self.pen.pu()
        self.pen.goto(x, y)
        self.pen.pd()

    def __first_star(self, line=50):
        """Draw first star"""
        self.pen.begin_fill()
        for _ in range(3):
            self.pen.fd(line)
            self.pen.lt(120)
        self.pen.end_fill()

    def __second_star(self, line=50):
        """Draw second star"""
        self.pen.begin_fill()
        for _ in range(3):
            self.pen.fd(line)
            self.pen.rt(120)
        self.pen.end_fill()

    def __star_pen_attrs(self):
        """Set attributes for pen drawing stars"""
        self.pen.color('white')
        self.pen.ht()
        self.pen.speed(0)

    def _draw_left_stars(self):
        """Draw stars on the Left side."""
        self.__star_pen_attrs()
        self.__move_pen(-350, 0)
        self.__first_star()
        self.__move_pen(-350, 30)
        self.__second_star()
        self.__move_pen(-350, -200)
        self.__first_star()
        self.__move_pen(-350, -170)
        self.__second_star()
        self.__move_pen(-350, 200)
        self.__first_star()
        self.__move_pen(-350, 230)
        self.__second_star()

    def _draw_right_stars(self):
        """Draw stars on the Right side"""
        self.__star_pen_attrs()
        self.__move_pen(350, 0)
        self.__first_star()
        self.__move_pen(350, 30)
        self.__second_star()
        self.__move_pen(350, -200)
        self.__first_star()
        self.__move_pen(350, -170)
        self.__second_star()
        self.__move_pen(350, 200)
        self.__first_star()
        self.__move_pen(350, 230)
        self.__second_star()

