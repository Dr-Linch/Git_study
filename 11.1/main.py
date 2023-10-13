user_name: str = input('Please enter your name!\n:')


def hello_user(name: str):
    start_answer: dict = {'yes': True, 'no': False}
    print(f'Hi {name}, glad to see you!')
    start_question: str = input('Do you want start the game?\n:')

    return start_answer[start_question.lower()]

print('1')
