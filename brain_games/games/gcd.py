#!/usr/bin/env python
from random import randint

TASK = 'Find the greatest common divisor of given numbers.'
LOWER_BOUND = 1
UPPER_BOUND = 100


def get_round():
    ran_num1 = randint(LOWER_BOUND, UPPER_BOUND)
    ran_num2 = randint(LOWER_BOUND, UPPER_BOUND)
    text_question = f'{ran_num1} {ran_num2}'
    correct_answer = get_answer(ran_num1, ran_num2)
    return text_question, correct_answer


def get_answer(num1, num2):
    while num2 != 0:
        if num1 > num2:
            num1, num2 = num2, num1
        num2 = num2 % num1
    return str(num1)
