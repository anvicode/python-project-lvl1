"""Add calc_brain_game."""

import prompt
import random

def calc():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('What is the result of the expression?')
    result = 0
    while result < 3:
        ran_num1 = random.randint(1, 25)
        ran_num2 = random.randint(1, 25)
        operations = ('+', '-', '*')
        ran_operation = random.choice(operations)
        answer = eval(f'{ran_num1} {ran_operation} {ran_num2}')
        # print(answer)
        print(f'Question: {ran_num1} {ran_operation} {ran_num2}')
        user_answer = prompt.integer(prompt='Your answer: ')
        if user_answer == answer:
            print('Correct!')
            result += 1
        else:
            print(f''''{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.''')
            print(f'''Let's try again, {user_name}!''')
    print(f'Congratulations, {user_name}!')