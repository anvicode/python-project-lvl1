#!/usr/bin/env python
import random

TASK = 'What is the result of the expression?'
LOWER_BOUND = 1
UPPER_BOUND = 25


def get_round():
    ran_num1 = random.randint(LOWER_BOUND, UPPER_BOUND)
    ran_num2 = random.randint(LOWER_BOUND, UPPER_BOUND)
    operations = random.choice('+-*')
    text_question = f'{ran_num1} {operations} {ran_num2}'
    correct_answer = str(eval(f'{ran_num1}{operations}{ran_num2}'))
    return text_question, correct_answer
