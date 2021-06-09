def print_play_field(play_field_list):
    '''Процедура отрисовывает игровое поле в консоле.'''
    print('   0  1  2')
    for i in range(0, 3):
        print(i, ' ', '  '.join(play_field_list[i]))


def one_game(score_user_comp):
    '''Процедура проведения одной партии.
       Аргументом функции является счёт до начала данной партии.
       Результат функции счёт по завершении данной партии (с учётом партий соверденных до этой).'''

    play_field_list = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]  # задаем модель, пока пустого, игрового поля
    print('Ходите первым.')
    print_play_field(play_field_list)
    move_user_str = input('Ваш ход. (строка, столбец): ')


    score_user_comp[0] = score_user_comp[0] + 1
    return score_user_comp


def tic_tac_toe():
    '''Программа-игра "Крестики-нолики".
       Игра осуществляется между пользователем и компьютером.
       Общение происходит через консоль. ПОле игры 3х3.'''
    begin_game = int(input('Здравствуйте! Хотите сыграть в "Крестики-нолики?" (да - 1, нет - 0): '))
    if begin_game:
        score_user_comp = [0, 0]  # переменная для ведения счёта [user, computer]
        score_user_comp = one_game(score_user_comp)
        while int(input('Ещё партию? (да - 1, нет - 0) ')):
            score_user_comp = one_game(score_user_comp)
            if score_user_comp[0] > score_user_comp[1]:
                favorite_to_post = ' в вашу пользу.'
            elif score_user_comp[0] < score_user_comp[1]:
                favorite_to_post = '. Компьютер ведёт.'
            else:
                favorite_to_post = '. Ничья.'
            print(f'Счёт {score_user_comp[0]} : {score_user_comp[1]}{favorite_to_post}')
    print('Может в другой раз? Счастливо!')


tic_tac_toe()

