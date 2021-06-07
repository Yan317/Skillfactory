import numpy as np


def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


def game_core_v1_2(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
        Но повторно не называем числа, которые уже называли.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    named_numbers = []
    while True:
        predict = np.random.randint(1, 101)  # предполагаемое число
        if predict in named_numbers:
            continue
        count += 1
        named_numbers.append(predict)
        if number == predict:
            return count  # выход из цикла, если угадали


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того,
       больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count  # выход из цикла, если угадали


def game_core_v3(number):
    '''Сначала устанавливаем любое random число. Тем самым разделяя рассматриваемый диапозн на две части.
       Полсе указания больше или меньше исключаем из диапозона поиска, ту часть чисел, которые заведомо не
       являются загаданным числом. Следующее любое random число ищем в пределах оставшегося диапозона.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    begin, end = 1, 100  # начало и конец диапозона чисел для random
    while True:
        count += 1
        predict = np.random.randint(begin, end+1)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали
        if number < predict:
            end = predict - 1
        if number > predict:
            begin = predict + 1


def game_core_v4(number):
    '''Алгоритм бинарного поиска.
        Генератор random числа в данном случае не нужен.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    begin, end = 1, 100  # начало и конец диапозона чисел для random
    while True:
        count += 1
        predict = int((begin + end)/2)  # согласно алгоритму всегда выбираем число в середине оставшегося диапозона
        # print(predict, number)  # для отладки - при желании можно посмотреть процесс происка
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
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# запускаем
print('1. Результат, если "тыкать пальцем в небо".')
score_game(game_core_v1)
print()
print('1.2. Результат, если "тыкать пальцем в небо", но уже не повторяться.')
score_game(game_core_v1_2)
print()
print('2. Результат, если "тыкать" один раз, а затем назыать все числа в направлении загаданного.')
score_game(game_core_v2)
print()
print('3. Результат алгоритма свойственный большенству людей.')
score_game(game_core_v3)
print('Я был очень удивлен, что эффективность данного спобоба так близка к бинарному поиску.')
print()
print('4. Результат, бинарного поиска.')
score_game(game_core_v4)
