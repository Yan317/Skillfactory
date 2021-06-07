import numpy as np


def game_core_v4(number):
    '''Алгоритм бинарного поиска.
        Генератор random числа в данном случае не нужен.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    begin, end = 1, 100  # начало и конец диапозона чисел для random
    while True:
        count += 1
        predict = int((begin + end)/2)  # согласно алгоритму всегда выбираем число в середине оставшегося диапозона
        print(begin, predict, end, number)  # для отладки - при желании можно посмотреть процесс происка
        if number == predict:
            return count  # выход из цикла, если угадали
        if number < predict:
            end = predict - 1
        if number > predict:
            begin = predict + 1


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=100)
    for number in random_array:
        count_ls.append(game_core(number))
        print()  # разделитель между эксперементами
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    print("Сумма попыток на всех опытах:", np.sum(count_ls))
    return score


score_game(game_core_v4)
# не очень правда понятно, почему среднее значение в 5.8 (математически) попыток превращается в 5....