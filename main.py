import turtle
import random
import time
import logging
import winsound
import sys
from helpers import resource_path, space_audio
from stars import draw_left_stars, draw_right_stars
from tkinter import *
from tkinter import messagebox


# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#Create handlers; set console handler level to debug and file handler to warning
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs.log', mode='a')
file_handler.setLevel(logging.INFO)
# create formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to console and file handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
# add console and file handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# screen
screen = turtle.Screen()
LENGTH, WIDTH = 1000, 900
screen.setup(LENGTH, WIDTH)
screen.colormode(255)
screen.bgcolor(0, 0, 0)
title = 'Space Math'
screen.title(title)
bg_img = resource_path(r"assets\images\space.gif")
sun_img = resource_path(r'assets\images\sun.gif')
moon_img = resource_path(r'assets\images\crescent_moon.png')
rocket_img = resource_path(r'assets\images\placidplace-rocket-12320_512.gif')
screen.bgpic(bg_img)
logger.info(f"Background image added {bg_img}")
screen.register_shape(name='sun', shape=sun_img)
screen.register_shape(name='moon', shape=moon_img)
screen.register_shape(name='rocket', shape=rocket_img)
screen.colormode(255)
# pen
pen = turtle.Turtle()
pen.ht()
pen.pencolor('yellow')
pen.pensize(2)
pen.speed(0)
# rocket
rocket = turtle.Turtle()
# font
font_name = 'Pacifico'
font_size = 50
font_type = 'italic'
# initialise variables
correct_answer = 0
suns = moons = skipped = 0   


def move_pen(x, y):
    """Move turtle to specified location"""
    pen.pu()
    pen.goto(x, y)
    pen.pd()

def setUp():
    space_audio()   # background music
    # write title
    move_pen(0, 200)
    pen.write(title, align='center', font=(font_name, font_size+20, font_type))
    # Draw stars
    screen.tracer(0)    # turn off animation so stars appear at once instead of drawing each star 
    logger.info('Animation turned off')
    draw_left_stars()
    draw_right_stars()
    logger.info("Stars drawn")
    screen.tracer(1) # turn on animation
    logger.info('Animation turned back on')


###### keep this here so it doesn't repeat in the loop for every question ######
setUp()
game_mode_mapping = {'1': 'Easy', '2': 'Medium', '3': 'Hard', '4': 'Pro'} 
game_mode = screen.textinput(
    "Level of Difficulty",
    """Enter '1' for easy, '2' for medium, '3' for hard, '4' for pro 
    or any other number to end the game""")
###############################################################################
    
def check_game_mode():
    """Difficulty level of the game"""
    min = max = 0
    if not game_mode.isdigit():
        messagebox.showerror('Invalid Entry', 
                             'Level of Difficulty should be a number from 1-4')
        logger.error(
            '''Input '%s' not accepted. 
            You can only enter an number from 1-4. 
            Exiting Game...''' % game_mode)
        sys.exit()
    else:
        match game_mode:
            case '1':
                min, max = 0, 9
            case '2':
                min, max = 10, 99
            case '3':
                min, max = 100, 500
            case '4':
                min, max = 500, 999
            case _:
               logger.warning('Exiting Game...')
               sys.exit()
    logger.info(
        '''Level: %s, Min value: %s, Max value: %s
        ''' % (game_mode_mapping[game_mode], min, max))
    return min, max    

def operation():
    """Return the chosen math operation"""
    min, max = check_game_mode()
    operators = ['+', '-', '*', '/', '^']
    number_1 = random.randint(min, max)
    operator = random.choice(operators)
    number_2 = random.randint(1, max)
    logger.info("Question: %d %s %d" % (number_1, operator, number_2))
    return number_1, operator, number_2, operators

def rocket_func():
    """Animated rocket"""
    rocket.shape('rocket')
    rocket.speed(3)
    rocket.pu()
    rocket.goto(0, -400)
    rocket.seth(90)
    rocket.fd(1000)
    rocket.ht()   

def countdown():
    """Countdown to start playing"""
    move_pen(0, 0)
    pen.pencolor('orange')
    pen.write('③', align='center', font=('Arial', font_size, 'italic'))
    time.sleep(1)
    pen.clear()
    pen.write('②', align='center', font=('Arial', font_size, 'italic'))
    time.sleep(1)
    pen.clear()
    pen.write('①', align='center', font=('Arial', font_size, 'italic'))
    time.sleep(1)
    pen.clear()
    pen.write('Go!', align='center', font=('Arial', font_size, 'italic'))
    time.sleep(1)
    pen.clear()

def show_message():
    """Display the title message"""
    msg = "Get a Sun or a Moon"
    hints = ('Hint (Addition): 2 + 10 = 12', 
             'Hint (Subtraction): 9 - 7 = 2', 
             'Hint (Multiplication): 6 * 10 = 60', 
             'Hint (Division): 20 / 5 = 4', 
             'Power: 3 ^ 3 = 3*3*3 = 27')
    move_pen(0, 400)
    for _ in range(1):
        r = random.randint(200, 255)
        g = random.randint(200, 255)
        b = random.randint(200, 255)
        pen.pencolor(r, g, b)
        pen.write(msg + '\n' + random.choice(hints), 
                  align='center', font=('Arial', 12, 'italic'))
        #time.sleep(5)
        #pen.clear()

def question_and_answer():
    """Return correct answer and user answer"""
    number_1, operator, number_2, _ = operation()
    pen.pencolor('yellow')
    move_pen(-100, 100)
    pen.write(number_1, align='center', font=(font_name, font_size, font_type))
    move_pen(0, 100)
    pen.write(operator, align='center', font=(font_name, font_size, font_type))
    move_pen(100, 100)
    pen.write(number_2, align='center', font=(font_name, font_size, font_type))
    move_pen(200, 100)
    pen.write("=", align='center', font=(font_name, font_size, font_type))
    
    user_answer = screen.textinput(
        "Answer", 
        """
        Enter the correct answer 
        (Approximate division questions to 2 decimal places): 
        """
        )
    try:
        user_answer = float(user_answer)
    except Exception as exc:
        logger.error("An error occured: %s" % exc)
    if operator == '+':
        correct_answer = number_1 + number_2
    elif operator == '-':
        correct_answer = number_1 - number_2
    elif operator == '*':
        correct_answer = number_1 * number_2
    elif operator == '/':
        correct_answer = round((number_1 / number_2), 2)
    elif operator == '^':
        correct_answer = number_1 ** number_2
    return correct_answer, user_answer

def mark_answer(): 
    """Mark answer""" 
    correct_answer, user_answer = question_and_answer()
    global suns, moons, skipped
    move_pen(0, -200)
    if user_answer is not None and isinstance(user_answer, float):
        if user_answer == correct_answer:
            right_turtle = turtle.Turtle()
            right_turtle.shape('sun')
            right_turtle.speed(0)
            pen.pencolor('green')
            pen.write(
                f'You got a sun! {user_answer} is correct', 
                align='center', 
                font=('Arial', 20, 'bold'))
            winsound.Beep(32767, 200)
            for _ in range(5):
                right_turtle.st()
                time.sleep(0.1)
                right_turtle.ht()     
            suns += 1
        else:
            wrong_turtle = turtle.Turtle()
            wrong_turtle.shape('moon')
            wrong_turtle.speed(0)
            pen.pencolor('red')
            pen.write(
                f'You got a moon! {user_answer} is incorrect', 
                align='center', font=('Arial', 20, 'bold'))  
            winsound.Beep(1000, 200)
            for _ in range(5):
                wrong_turtle.st()
                time.sleep(0.1)
                wrong_turtle.ht()
            moons += 1
    else:
        skipped += 1
    logger.info(f'correct answer {correct_answer}')
    logger.info(f'user answer {user_answer}')
    return suns, moons, skipped

def analytics():
    move_pen(-300, -400)
    pen.pencolor('yellow')
    pen.write(
        f"{suns} ☀️", align='center', font=('Comic Sans MS', 30, 'bold')
        )
    move_pen(-100, -400)
    pen.pencolor('white')
    pen.write(
        f"{moons} 🌙", 
        align='center', font=('Comic Sans MS', 30, 'bold'))
    move_pen(100, -400)
    pen.pencolor('gray')
    pen.write(
        f"{skipped} skipped", 
        align='center', font=('Comic Sans MS', 30, 'italic'))
    move_pen(300, -400)
    pen.pencolor('orange')
    pen.write(
        f"{int(no_of_tries)-int(no_of_questions)} left", 
        align='center', font=('Comic Sans MS', 30, 'italic'))

def game_over_func():
    """Game over"""
    move_pen(0, 0)
    pen.pencolor('red')
    end_msg = 'Game Over'
    logger.info(end_msg)
    pen.write(end_msg, align='center', font=(font_name, font_size, font_type))


if __name__ == '__main__':
    game_over = False
    no_of_questions = 0
    no_of_tries = screen.textinput(
        "Number of questions", 
        """Enter the number of questions you would like to answer 
        or any other character to exit""")
    if no_of_tries is None or not no_of_tries.isdigit():
        logger.warning('Exiting Game...')
        sys.exit()
    else:
        countdown()
        rocket_func()
        while not game_over and no_of_questions < int(no_of_tries):
            show_message()
            suns, moons, skipped = mark_answer()
            no_of_questions += 1
            pen.clear()
            analytics()
        else:
            pen.clear()
            game_over_func()
        
        analytics()
        # loggings
        logger.info(f'suns {suns}')
        logger.info(f'moons {moons}')
        logger.info(f'Skipped {skipped}')
        logger.info("Total number of questions: %s" % no_of_questions)
    screen.mainloop()
