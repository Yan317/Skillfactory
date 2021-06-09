import numpy as np


# список нборов адресов, представляющих из себя "линии" возможных решений
solution_address_set = [[(0, 0), (0, 1), (0, 2)],
                        [(1, 0), (1, 1), (1, 2)],
                        [(2, 0), (2, 1), (2, 2)],
                        [(0, 0), (1, 0), (2, 0)],
                        [(0, 1), (1, 1), (2, 1)],
                        [(0, 2), (1, 2), (2, 2)],
                        [(0, 0), (1, 1), (2, 2)],
                        [(2, 0), (1, 1), (0, 2)],
                        ]


def print_play_field(play_field_list):
    '''Процедура отрисовывает игровое поле в консоле.'''
    print('    0  1  2')  # нумирация столбцов
    for i in range(0, 3):  # цикл отрисовки строк
        print(i, ' ', '  '.join(play_field_list[i]))


def checking_for_win(play_field_list):
    '''Функция проверяет не наступил ли выигрыш.
       Если наступил, то возвращает победителя ("x" или "o").
       Аргументом на входе функции является игровое поле, которое надо оценить.'''
    for line_list in solution_address_set:
        winner = ''
        cell = line_list[0]
        if play_field_list[cell[0]][cell[1]] != '-':
            winner = play_field_list[cell[0]][cell[1]]
            cell = line_list[1]
            if winner == play_field_list[cell[0]][cell[1]]:
                cell = line_list[2]
                if winner == play_field_list[cell[0]][cell[1]]:
                    break
        winner = ''
    return winner


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
        # проверяем не появился ли победитель
        winner = checking_for_win(play_field_list)
        if winner:
            if winner == 'x':
                print_play_field(play_field_list)  # выводим итоговую ситуацию на игровом поле
                print('Вы победили!')
                score_user_comp[0] += 1     # засчитываем очко игроку
            else:
                print_play_field(play_field_list)  # выводим итоговую ситуацию на игровом поле
                print('Победил компьютер.')
                score_user_comp[1] += 1     # засчитываем очко компьютеру
            break
    if not winner:
        print('Ничья!')
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
                favorite_to_post = '. Счёт выровнялся.'
            print(f'Счёт {score_user_comp[0]} : {score_user_comp[1]}{favorite_to_post}')
    print('Может в другой раз? Счастливо!')


tic_tac_toe()

