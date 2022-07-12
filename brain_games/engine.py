import prompt

ROUND_COUNT = 3


def run(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.TASK)
    for _ in range(ROUND_COUNT):
        text_question, correct_answer = game.get_round()
        print(f'Question: {text_question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
