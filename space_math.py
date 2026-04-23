import turtle
import random
import time
import sys
from utils import Logger, Helpers
from stars import DrawStars
from tkinter import *
from tkinter import messagebox


class SpaceMath:
    def __init__(self): 
        self.screen = turtle.Screen()
        self.pen = turtle.Turtle()
        self.rocket = turtle.Turtle()
        self.logger = Logger(name=__name__).logger
        self.font_name = 'Pacifico'
        self.font_size = 50
        self.font_type = 'italic'
        self.game_mode_mapping = {}
        self.game_mode = ''
        self.__screen_settings()
        self.__add_assets()
        self.__pen_settings()
        self.__setUp() 
        self.__game_mode_settings()

    def __screen_settings(self):
        self.LENGTH, self.WIDTH = 1200, 900
        self.screen.setup(self.LENGTH, self.WIDTH)
        self.screen.colormode(255)
        self.screen.bgcolor(0, 0, 0)
        self.title = 'Space Math'
        self.screen.title(self.title)
        self.screen.colormode(255)

    def __add_assets(self):
        """Add game assets"""
        self.helpers = Helpers()
        bg_img = self.helpers._resource_path(r"assets\images\space.gif")
        sun_img = self.helpers._resource_path(r'assets\images\sun.gif')
        moon_img = self.helpers._resource_path(r'assets\images\crescent_moon.png')
        rocket_img = self.helpers._resource_path(r'assets\images\placidplace-rocket-12320_512.gif')
        self.screen.bgpic(bg_img)
        self.logger.info(f"Background image added {bg_img}")
        self.screen.register_shape(name='sun', shape=sun_img)
        self.screen.register_shape(name='moon', shape=moon_img)
        self.screen.register_shape(name='rocket', shape=rocket_img)
    
    def __pen_settings(self):  
        """Pen settings"""
        self.pen.ht()
        self.pen.pencolor('yellow')
        self.pen.pensize(2)
        self.pen.speed(0)
 
    def move_pen(self, x, y):
        """Move turtle to specified location"""
        self.pen.pu()
        self.pen.goto(x, y)
        self.pen.pd()

    def __setUp(self):
        self.helpers._space_audio()   # background music
        self.stars = DrawStars()
        # write title
        self.move_pen(0, 300)
        self.pen.write(self.title, align='center', font=(self.font_name, self.font_size, self.font_type))
        self.screen.tracer(0)    # turn off animation so stars appear at once instead of drawing each star 
        self.logger.info('Animation turned off')
        self.stars._draw_left_stars()
        self.stars._draw_right_stars()
        self.logger.info("Stars drawn")
        self.screen.tracer(1) # turn on animation
        self.logger.info('Animation turned back on')

    def __game_mode_settings(self):
        """Settings for level of difficulty"""
        self.game_mode_mapping = {'1': 'Easy', '2': 'Medium', '3': 'Hard', '4': 'Pro'} 
        self.game_mode = self.screen.textinput(
            "Level of Difficulty",
            """Enter '1' for easy, '2' for medium, '3' for hard, '4' for pro 
            or any other number to end the game""")
    
    def check_game_mode(self):
        """Difficulty level of the game"""
        min = max = 0
        if not self.game_mode.isdigit():
            messagebox.showerror('Invalid Entry', 
                                'Level of Difficulty should be a number from 1-4')
            self.logger.error(
                '''Input '%s' not accepted. 
                You can only enter an number from 1-4. 
                Exiting Game...''' % self.game_mode)
            sys.exit()
        else:
            match self.game_mode:
                case '1':
                    min, max = 0, 9
                case '2':
                    min, max = 10, 99
                case '3':
                    min, max = 100, 299
                case '4':
                    min, max = 300, 500
                case _:
                    self.logger.warning('Exiting Game...')
                    sys.exit()
        self.logger.info(
            '''Level: %s, Min value: %s, Max value: %s
            ''' % (self.game_mode_mapping[self.game_mode], min, max))
        return min, max    

    def rocket_func(self):
        """Animated rocket"""
        self.rocket.shape('rocket')
        self.rocket.speed(10)
        self.rocket.pu()
        self.rocket.goto(0, -400)
        self.rocket.seth(90)
        self.rocket.fd(1000)
        self.rocket.ht()   

    def countdown(self):
        """Countdown to start playing"""
        self.move_pen(0, 0)
        self.pen.pencolor('orange')
        self.pen.write('③', align='center', font=('Arial', self.font_size, 'italic'))
        time.sleep(0.5)
        self.pen.clear()
        self.pen.write('②', align='center', font=('Arial', self.font_size, 'italic'))
        time.sleep(0.5)
        self.pen.clear()
        self.pen.write('①', align='center', font=('Arial', self.font_size, 'italic'))
        time.sleep(0.5)
        self.pen.clear()
        self.pen.write('Go!', align='center', font=('Arial', self.font_size, 'italic'))
        time.sleep(0.5)
        self.pen.clear()

    def show_message(self):
        """Display the title message"""
        msg = "Get a Sun or a Moon"
        hints = ('Hint (Addition): 2 + 10 = 12', 
                'Hint (Subtraction): 9 - 7 = 2', 
                'Hint (Multiplication): 6 * 10 = 60', 
                'Hint (Division): 20 / 5 = 4', 
                'Power: 3 ^ 3 = 3*3*3 = 27')
        self.move_pen(0, 400)
        self.pen.pencolor(random.randint(200, 255), random.randint(200, 255), 
                          random.randint(200, 255))
        self.pen.write(msg + '\n' + random.choice(hints), align='center', 
                       font=('Arial', 12, 'italic'))
