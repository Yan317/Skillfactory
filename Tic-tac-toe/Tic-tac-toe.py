import numpy as np


def print_play_field(play_field_list):
    '''Процедура отрисовывает игровое поле в консоле.'''
    print('    0  1  2')  # нумирация столбцов
    for i in range(0, 3):  # цикл отрисовки строк
        print(i, ' ', '  '.join(play_field_list[i]))


def move_user(play_field_list):
    '''Функция обработкит хода пользователся.
       На вход функции подается игровое поле до хода пользователся.
       На выходе функции игровое поле после с учётом хода пользователся.'''
    while True:
        print_play_field(play_field_list)  # выводим текущую ситуацию на игровом поле
        move_user_str = input('Ваш ход. (строка, столбец): ')
        move_user_list = list(map(int, move_user_str.split(',')))  # преобразуем в список координат
        if move_user_list[0] > 2 or move_user_list[1] > 2:
            print('На поле нет такой ячейки. Попробуйте ещё раз.')
            continue
        if play_field_list[move_user_list[0]][move_user_list[1]] == '-':
            play_field_list[move_user_list[0]][move_user_list[1]] = 'x'
            break
        else:
            print('Указанная вами ячейка уже занята. Попробуйте ещё раз.')
    return play_field_list


def move_computer(play_field_list):
    '''Функция обработки хода компьютером.
       На вход функции подается игровое поле до хода пользователся.
       На выходе функции игровое поле после с учётом хода пользователся.
       Компьютер делает свой ход на угад - в любую свободную ячейку, "не думая".'''

    # для начала выясним количество возможных ходов (оставшихся пустых ячеек)
    play_field_list_line = sum(play_field_list, [])  # приведём список списков "в одну линию"
    count_moves_left = len(list(filter(lambda m: m == '-', play_field_list_line)))

    # выбор хода и проставление "нолика"
    move_select = np.random.randint(1, count_moves_left)
    for row in range(len(play_field_list)):
        for column in range(len(play_field_list[row])):
            if play_field_list[row][column] == '-':
                move_select -= 1
                if not move_select:
                    play_field_list[row][column] = 'o'

    return play_field_list


def one_game(score_user_comp):
    '''Процедура проведения одной партии.
       Аргументом функции является счёт до начала данной партии.
       Результат функции счёт по завершении данной партии (с учётом партий соверденных до этой).'''

    play_field_list = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]  # задаем модель, пока пустого, игрового поля
    print('Ходите первым.')
    move_user_bool = True  # переменная определяющая чей ход
    while '-' in sum(play_field_list, []):  # проверка наличия "пустых" ячеек для хода
        if move_user_bool:
            play_field_list = move_user(play_field_list)
            move_user_bool = False
        else:
            play_field_list = move_computer(play_field_list)
            move_user_bool = True
        # проверяем не закончилась ли игра
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

