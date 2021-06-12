import numpy as np


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed()  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=100)
    for number in random_array:
        count_ls.append(game_core(number))
        print()  # разделитель между эксперементами
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    print("Сумма попыток на всех опытах:", np.sum(count_ls))
    return score


def game_score(number):
    '''blu-blu
    '''
    count = 1
    minmum = 1
    maxmum = 101

    predict = (minmum + maxmum) // 2
    print(minmum, predict, maxmum, number)  # для отладки - при желании можно посмотреть процесс происка

    while number != predict:
        count += 1
        if number > predict:
            minmum = predict
        else:
            maxmum = predict

        predict = (minmum + maxmum) // 2
        print(minmum, predict, maxmum, number)  # для отладки - при желании можно посмотреть процесс происка

    return count


score_game(game_score)
