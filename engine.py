import random


NUMS = '0123456789'


def make_a_number():
    number_final = ''
    while len(number_final) < 4:
        num_chosen = random.choice(NUMS)
        if num_chosen not in number_final:
            number_final += num_chosen
    return number_final


def get_users_guess():
    while True:
        guess = input('Ваше число:\n> ')
        if len(guess) == 4:
            for char in guess:
                if char not in NUMS:
                    print('Это должны быть цифры!')
                    break
                if guess.count(char) > 1:
                    print('Не должно быть одинаковых цифр!')
                    break
            else:
                return guess
        else:
            print('Число должно быть четырехзначным!')


def check_if_correct(users_num, right_answer):
    if users_num == right_answer:
        return 'Угадал!'
    bulls = []
    cows = []
    for i in range(4):
        if users_num[i] == right_answer[i]:
            bulls.append(users_num[i])
    for char in users_num:
        if char in right_answer:
            if char not in bulls and char not in cows:
                cows.append(char)
    return f'Быки: {len(bulls)}.\nКоровы: {len(cows)}'


