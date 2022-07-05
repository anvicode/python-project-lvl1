"""Add cli."""

import prompt


def welcome_user():
    """Add welcome User."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
