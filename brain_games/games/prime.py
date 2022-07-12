#!/usr/bin/env python
from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
LOWER_BOUND = 2
UPPER_BOUND = 100


def get_round():
    number = randint(LOWER_BOUND, UPPER_BOUND)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer


def is_prime(number):
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                return False
        return True
    return False
