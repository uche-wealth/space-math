import turtle
import random
import time


# screen
screen = turtle.Screen()
LENGTH, WIDTH = 800, 700
screen.setup(LENGTH, WIDTH)
screen.colormode(255)
screen.bgcolor(0, 0, 0)
screen.title('Sun or Moon Game')
bg_img = "images\\space.gif"
sun_img = 'images\\sun.gif'
moon_img = 'images\\crescent_moon.png'
screen.bgpic(bg_img)
screen.register_shape(name='sun', shape=sun_img)
screen.register_shape(name='moon', shape=moon_img)
screen.colormode(255)
# pen
pen = turtle.Turtle()
pen.pencolor('yellow')
pen.pensize(2)

# font
font_name = 'Pacifico'
font_size = 50
font_type = 'italic'
correct_answer = suns = moons = 0   # initialise variables

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

def move_pen(x, y):
    """Move turtle to specified location"""
    pen.pu()
    pen.goto(x, y)
    pen.pd()

def show_message():
    """Display the title message"""
    msg = "Get a sun 🌞 for correct answers or a moon 🌛 for incorrect answers"
    move_pen(LENGTH-800, WIDTH-400)
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
            pen.pencolor('green')
            pen.write(
                f'You got a sun! {user_answer} is correct', 
                align='center', 
                font=('Arial', 20, 'bold'))
            right_turtle = turtle.Turtle()
            right_turtle.shape('sun')
            for _ in range(10):
                right_turtle.st()
                time.sleep(0.1)
                right_turtle.ht()     
            suns += 1
        else:
            pen.pencolor('red')
            pen.write(
                f'You got a moon! {user_answer} is incorrect', 
                align='center', font=('Arial', 20, 'bold'))
            wrong_turtle = turtle.Turtle()
            wrong_turtle.shape('moon')
            for _ in range(10):
                wrong_turtle.st()
                time.sleep(0.1)
                wrong_turtle.ht()
            moons += 1

    print(f'correct answer {correct_answer}')
    print(f'user answer {user_answer}')
    return suns, moons


if __name__ == '__main__':
    game_over = False
    no_of_questions = 0
    while not game_over:
        pen.ht()
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
        #screen.mainloop()



