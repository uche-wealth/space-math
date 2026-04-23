import turtle
import random
import time
import winsound
import sys
from utils import Logger
from space_math import SpaceMath

        
class Main(SpaceMath):
    """Model questions and answers"""
    def __init__(self):
        self.correct_answer = self.suns = self.moons = self.skipped = 0 
        self.no_of_tries = ''
        self.no_of_questions = 0
        
        super().__init__()
        self.logger = Logger(name=__name__).logger
    
    def operation(self):
        """Return the chosen arithmetic operation"""
        min, max = self.check_game_mode()
        operators = ['+', '-', '*', '/', '^']
        number_1 = random.randint(min, max)
        operator = random.choice(operators)
        number_2 = random.randint(1, max)
        self.logger.info("Question: %d %s %d" % (number_1, operator, number_2))
        return number_1, operator, number_2, operators

    def write_question(self):
        """Write question to the screen"""
        number_1, operator, number_2, _ = self.operation()
        self.pen.pencolor('yellow')
        self.move_pen(-100, 100)
        self.pen.write(number_1, align='center', 
                       font=(self.font_name, self.font_size, self.font_type))
        self.move_pen(0, 100)
        self.pen.write(operator, align='center', 
                       font=(self.font_name, self.font_size, self.font_type))
        self.move_pen(100, 100)
        self.pen.write(number_2, align='center', 
                       font=(self.font_name, self.font_size, self.font_type))
        self.move_pen(200, 100)
        self.pen.write("=", align='center', 
                       font=(self.font_name, self.font_size, self.font_type))
        return number_1, operator, number_2 # return here for use in marking  

    def get_answers(self):
        """Return correct answer and user answer"""
        number_1, operator, number_2 = self.write_question()
        user_answer = self.screen.textinput(
            "Answer", 
            """
            Enter the correct answer 
            (Approximate division questions to 2 decimal places): 
            """
            )
        try:
            user_answer = float(user_answer)
        except Exception as exc:
            self.logger.error("An error occured: %s" % exc)
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

    def mark_answer(self): 
        """Mark answer""" 
        self.correct_answer, user_answer = self.get_answers()
        self.move_pen(0, -200)
        if user_answer is not None and isinstance(user_answer, float):
            if user_answer == self.correct_answer:
                right_turtle = turtle.Turtle()
                right_turtle.shape('sun')
                right_turtle.speed(0)
                self.pen.pencolor('green')
                self.pen.write(
                    f'You got a sun! {user_answer} is correct', 
                    align='center', 
                    font=('Arial', 20, 'bold'))
                winsound.Beep(32767, 200)
                for _ in range(3):
                    right_turtle.st()
                    time.sleep(0.1)
                    right_turtle.ht()     
                self.suns += 1
            else:
                wrong_turtle = turtle.Turtle()
                wrong_turtle.shape('moon')
                wrong_turtle.speed(0)
                self.pen.pencolor('red')
                self.pen.write(
                    f'You got a moon! {user_answer} is incorrect', 
                    align='center', font=('Arial', 20, 'bold'))  
                winsound.Beep(1000, 200)
                for _ in range(3):
                    wrong_turtle.st()
                    time.sleep(0.1)
                    wrong_turtle.ht()
                self.moons += 1
        else:
            self.skipped += 1
        self.logger.info(
            f'correct answer {self.correct_answer}\nuser answer {user_answer}')
        return self.suns, self.moons, self.skipped

    def analytics(self):
        self.move_pen(-300, -400)
        self.pen.pencolor('yellow')
        self.pen.write(
            f"{self.suns} ☀️", align='center', font=('Comic Sans MS', 30, 'bold')
            )
        self.move_pen(-100, -400)
        self.pen.pencolor('white')
        self.pen.write(
            f"{self.moons} 🌙", 
            align='center', font=('Comic Sans MS', 30, 'bold'))
        self.move_pen(100, -400)
        self.pen.pencolor('gray')
        self.pen.write(
            f"{self.skipped} skipped", 
            align='center', font=('Comic Sans MS', 30, 'italic'))
        self.move_pen(300, -400)
        self.pen.pencolor('orange')
        self.pen.write(
            f"{int(self.no_of_tries)-int(self.no_of_questions)} left", 
            align='center', font=('Comic Sans MS', 30, 'italic'))

    def game_over_func(self):
        """Game over"""
        self.move_pen(0, 0)
        self.pen.pencolor('red')
        end_msg = 'Game Over'
        self.logger.info(end_msg)
        self.pen.write(end_msg, align='center', 
                       font=(self.font_name, self.font_size, self.font_type))


    def main(self):
        """Main Game loop"""
        game_over = False
        self.no_of_tries = self.screen.textinput(
            "Number of questions", 
            """Enter the number of questions you would like to answer 
            or any other character to exit""")
        if self.no_of_tries is None or not self.no_of_tries.isdigit():
            self.logger.warning('Exiting Game...')
            sys.exit()
        else:
            self.countdown()
            self.rocket_func()
            while not game_over and self.no_of_questions < int(self.no_of_tries):
                self.show_message()
                suns, moons, skipped = self.mark_answer()
                self.no_of_questions += 1
                self.pen.clear()
                self.analytics() # this shows real time analytics
            else:
                self.pen.clear()
                self.game_over_func()
            
            self.analytics() # this shows analytics after game
            # loggings
            self.logger.info(f'\nsuns {suns}\nmoons {moons}\nSkipped {skipped}')
            self.logger.info("Total number of questions: %s" % self.no_of_questions)

if __name__ == '__main__':
    run_game = Main()
    run_game.main()
    turtle.done()
