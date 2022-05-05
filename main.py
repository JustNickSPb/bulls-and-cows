from engine import *


if __name__ == '__main__':
    comp_num = make_a_number()
    while True:
        guess = get_users_guess()
        answer = check_if_correct(guess, comp_num)
        if answer == 'Угадал!':
            break
        print(answer)
    print('Поздравляем, Вы победили!')
