"""Add prime_brain_game."""

import prompt
import random

def prime():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    result = 0
    while result < 3:
        number = random.randint(2, 100)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if is_prime(number) and user_answer == 'yes':
            print('Correct!')
            result += 1
        elif is_prime(number) and user_answer == 'no':
            print(''''no' is wrong answer ;(. Correct answer was 'yes'.''')
            print(f'''Let's try again, {user_name}!''')
        elif is_prime(number) == False and user_answer == 'yes':
            print(''''yes' is wrong answer ;(. Correct answer was 'no'.''')
            print(f'''Let's try again, {user_name}!''')
        elif is_prime(number) == False and user_answer == 'no':
            print('Correct!')
            result += 1
    print(f'Congratulations, {user_name}!')

def is_prime(number):
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                return False
        return True
    return False