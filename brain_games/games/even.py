"""Add logic_brain_even"""

import prompt
from random import randint

def even():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    result = 0
    while result < 3:
        number = randint(1, 20)
        even_num = (number % 2) == 0
        odd_num = (number % 2) == 1
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if even_num and answer == 'yes':
            print('Correct!')
            result += 1
        elif even_num and answer == 'no':
            print(''''no' is wrong answer ;(. Correct answer was 'yes'.''')
            print(f'''Let's try again, {user_name}!''')
        elif odd_num and answer == 'no':
            print('Correct!')
            result += 1
        elif odd_num and answer == 'yes':
            print(''''yes' is wrong answer ;(. Correct answer was 'no'.''')
            print(f'''Let's try again, {user_name}!''')
        elif (answer != 'yes' or 'no'):
            print(f'{answer} is wrong answer ;(')
            print(f'''Let's try again, {user_name}!''')
    print(f'Congratulations, {user_name}!')