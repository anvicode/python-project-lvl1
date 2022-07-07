"""Add gcd_brain_game."""

import math
import prompt
import random

def gcd():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Find the greatest common divisor of given numbers.')
    result = 0
    while result < 3:
        ran_num1 = random.randint(1, 100)
        ran_num2 = random.randint(1, 100)
        answer = math.gcd(ran_num1, ran_num2)
        print(f'Question: {ran_num1} {ran_num2}')
        user_answer = prompt.integer(prompt='Your answer: ')
        if user_answer == answer:
            print('Correct!')
            result += 1
        else:
            print(f''''{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.''')
            print(f'''Let's try again, {user_name}!''')
    print(f'Congratulations, {user_name}!')