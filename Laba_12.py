"""
Вариант 13:
Вычислить сумму знакопеременного ряда (|х^(n-1)|)/(n-1)!, где х-матрица ранга к (к и матрица, задаются случайным
образом), n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после
запятой. У алгоритма д.б. линейная сложность. Знак первого слагаемого - случайный."""

import numpy as np
from random import choice, randint
from decimal import Decimal, getcontext


def s_sum(matrix_start, accuracy):
    n = 1
    summ = 0
    factorial = 1
    matrix = matrix_start
    sign = choice([-1, 1])

    # Начинаем бесконечный цикл для вычисления ряда
    while True:
        curr_term = Decimal(np.linalg.det(matrix) / factorial)
        # decimal, что позволяет сохранять числа после запятой, даже при больших значениях самого числа
        summ += sign * curr_term

        # Проверяем, достигли ли заданной точности t
        if abs(curr_term) < 1 / (10 ** accuracy):
            break

        # Параметры для следующего слагаемого
        n += 1
        sign = -sign
        matrix *= matrix
        factorial *= (n-1)

    return summ


try:
    t = int(input('Введите число t, являющееся кол-вом знаков после запятой: '))
    while t > 300 or t < 1:
        t = int(input('Введите число t, больше 0:\n'))

    # Генерация случайного значения k и матрицы x
    k = randint(2, 10)
    x = np.round(np.random.uniform(-1, 1, (k, k)), 3)

    print('\nМатрица:\n', x)

    # Установка технической точности вычислений с учетом заданной
    getcontext().prec = t + 100

    result = s_sum(x, t)

    print(f"\nСумма ряда с точностью {t} знаков после запятой: {result:.{t}f}".rstrip('0').rstrip('.'))

except ValueError:
    print('\nПерезапустите программу и введите число.')
