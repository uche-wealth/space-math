import turtle
import random
import time
import logging
import winsound
from pygame import mixer
from stars import draw_left_stars, draw_right_stars


logging.basicConfig(level=logging.INFO)
# screen
screen = turtle.Screen()
LENGTH, WIDTH = 800, 700
screen.setup(LENGTH, WIDTH)
screen.colormode(255)
screen.bgcolor(0, 0, 0)
title = 'Space Math'
screen.title(title)
bg_img = r"images\space.gif"
sun_img = r'images\sun.gif'
moon_img = r'images\crescent_moon.png'
screen.bgpic(bg_img)
logging.info(f"Background image added {bg_img}")
screen.register_shape(name='sun', shape=sun_img)
screen.register_shape(name='moon', shape=moon_img)
screen.colormode(255)

# pen
pen = turtle.Turtle()
pen.pencolor('yellow')
pen.pensize(2)
pen.speed(0)
pen.ht()

# font
font_name = 'Pacifico'
font_size = 50
font_type = 'italic'

correct_answer = 0
suns = 0
moons = 0   # initialise variables
# background music
bg_audio = r'audio\freesound_community-space-adventure-29296.mp3'
mixer.init()
mixer.music.load(bg_audio)
mixer.music.play(loops=-1)
logging.info(f"Background music playing {bg_audio}")

def move_pen(x, y):
    """Move turtle to specified location"""
    pen.pu()
    pen.goto(x, y)
    pen.pd()

# write title
move_pen(0, 300)
pen.write(title, align='center', font=(font_name, font_size-15, font_type))
# Draw stars
screen.tracer(0)    # turn off animation so stars appear at once instead of drawing each star 
logging.info('Animation turned off')
draw_left_stars()
draw_right_stars()
screen.tracer(1) # turn on animation
logging.info('Animation turned back on')
# keep this here so it doesn't repeat in the loop for every question
game_mode = screen.textinput(
    "Choose Level of Difficulty",
    "Enter '1' for easy, '2' for medium, '3' for hard or '4' for pro")

def check_game_mode():
    """Difficulty level of the game"""
    min = max = 0
    
    match game_mode:
        case '1':
            min, max = 0, 9
        case '2':
            min, max = 10, 99
        case '3':
            min, max = 100, 999
        case '4':
            min, max = 1000, 9999
        case _:
            print("We didn't understand what you entered")
    return min, max

def operation():
    """Return the chosen math operation"""
    min, max = check_game_mode()
    operators = ['+', '-', '*', '/']
    number_1 = random.randint(min, max)
    operator = random.choice(operators)
    number_2 = random.randint(1, max)
    return number_1, operator, number_2, operators

def show_message():
    """Display the title message"""
    msg = "Get a sun 🌞 for correct answers or a moon 🌛 for incorrect answers"
    move_pen(LENGTH-800, WIDTH-450)
    for _ in range(1):
        r = random.randint(200, 255)
        g = random.randint(200, 255)
        b = random.randint(200, 255)
        pen.pencolor(r, g, b)
        pen.write(msg, align='center', font=('Arial', 12, 'italic'))
        time.sleep(2)
        pen.clear()

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
    print('Question:', number_1, operator, number_2)
    user_answer = screen.numinput(
        "Answer", "Enter the correct answer (for division: to 2 decimal place): "
        )
    if operator == '+':
        correct_answer = number_1 + number_2
    elif operator == '-':
        correct_answer = number_1 - number_2
    elif operator == '*':
        correct_answer = number_1 * number_2
    elif operator == '/':
        correct_answer = round((number_1 / number_2), 2)
    else:
        pass
    return correct_answer, user_answer

def mark_answer(): 
    """Mark answer""" 
    correct_answer, user_answer = question_and_answer()
    global suns, moons
    move_pen(0, -200)
    if user_answer is not None:
        if user_answer == correct_answer:
            right_turtle = turtle.Turtle()
            right_turtle.shape('sun')
            pen.pencolor('green')
            pen.write(
                f'You got a sun! {user_answer} is correct', 
                align='center', 
                font=('Arial', 20, 'bold'))
            winsound.Beep(32767, 200)
            for _ in range(10):
                right_turtle.st()
                time.sleep(0.1)
                right_turtle.ht()     
            suns += 1
        else:
            wrong_turtle = turtle.Turtle()
            wrong_turtle.shape('moon')
            pen.pencolor('red')
            pen.write(
                f'You got a moon! {user_answer} is incorrect', 
                align='center', font=('Arial', 20, 'bold'))  
            winsound.Beep(1000, 200)
            for _ in range(10):
                wrong_turtle.st()
                time.sleep(0.1)
                wrong_turtle.ht()
            moons += 1

    print(f'correct answer {correct_answer}')
    print(f'user answer {user_answer}')
    return suns, moons

def game_over_func():
    """Game over"""
    move_pen(0, 0)
    pen.pencolor('red')
    end_msg = 'Game Over'
    print(end_msg)
    pen.write(end_msg, align='center', font=(font_name, font_size, font_type))


if __name__ == '__main__':
    game_over = False
    no_of_questions = 0
    no_of_tries = 3
    exit_duration = 5
    while not game_over and no_of_questions < no_of_tries:
        show_message()
        suns, moons = mark_answer()
        no_of_questions += 1
        pen.clear()
        move_pen(-100, -200)
        pen.pencolor('yellow')
        pen.write(
            f"{suns} ☀️", align='center', font=('Comic Sans MS', 20, 'bold')
            )
        move_pen(100, -200)
        pen.pencolor('white')
        pen.write(
            f"{moons} 🌙", 
            align='center', font=('Comic Sans MS', 20, 'bold'))
        print(f'suns {suns}')
        print(f'moons {moons}')
        print("Total number of questions: %s" % no_of_questions)
    else:
        game_over_func()
        logging.info("Game Over... Exiting in %s seconds" % exit_duration)
    #screen.mainloop()
    time.sleep(exit_duration)   # sleep and exit afterwards



