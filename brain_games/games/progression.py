"""Add progression_brain_game."""

import prompt
import random

LOWER_BOUND = 1
INITIAL_UPPER_BOUND = 20
INCREASE_UPPER_BOUND = 5

def progression():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('What number is missing in the progression?')
    length = 10
    result = 0
    while result < 3:
        initial = random.randint(LOWER_BOUND, INITIAL_UPPER_BOUND)
        increase = random.randint(LOWER_BOUND, INCREASE_UPPER_BOUND)
        progression = get_progression(initial, increase, length)
        key = random.choice(progression)
        text_question = ' '.join([
            '..' if num == key else str(num) for num in progression
        ])
        print(f'Question: {text_question}')
        user_answer = prompt.integer(prompt='Your answer: ')
        if user_answer == key:
                print('Correct!')
                result += 1
        else:
            print(f''''{user_answer}' is wrong answer ;(. Correct answer was '{key}'.''')
            print(f'''Let's try again, {user_name}!''')
    print(f'Congratulations, {user_name}!')

def get_progression(initial, increase, length):
    max_num = initial + (increase * length)
    return range(initial, max_num, increase)