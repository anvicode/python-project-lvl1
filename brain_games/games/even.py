#!/usr/bin/env python
from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
LOWER_BOUND = 1
UPPER_BOUND = 20


def get_round():
    number = randint(LOWER_BOUND, UPPER_BOUND)
    text_question = number
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return text_question, correct_answer


def is_even(number):
    return (number % 2) == 0
