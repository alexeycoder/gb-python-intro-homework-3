# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным ненулевым значением дробной части элементов.
# Минимальное значение дробной части отличное от нуля, у целых чисел дробной части нет их в расчет не берем
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
import common
from common import ForeColor
from math import trunc

# consts:

WARN_OUT_OF_RANGE = 'Ошибка: Количетсво элементов не может быть меньше одного! ' + \
    common.PLEASE_REPEAT

DIGITS_PRECISION = 3
EPSILON = 1E-6

# methods:


def get_fractional_part(value, digits):
    return round(value - trunc(value), digits)


def get_fractional_nonzero_min_max(floats_list, epsilon, digits, signed=False):
    frac_min = None
    frac_max = None
    for value in floats_list:
        frac_value = get_fractional_part(value, digits)
        if not signed:
            frac_value = abs(frac_value)
        if (abs(frac_value) > epsilon):
            if (frac_min is None or frac_value < frac_min):
                frac_min = frac_value
            if (frac_max is None or frac_value > frac_max):
                frac_max = frac_value
    return (frac_min, frac_max)


def get_random_float(min_value, max_value):
    rnd_value = min_value + (max_value - min_value)*random.random()
    return round(rnd_value, 3)


def create_list_random_float(length, min_value, max_value):
    return [get_random_float(min_value, max_value) for _ in range(length)]


# main flow:

user_answer = True

while(user_answer):
    common.console_clear()
    common.print_title('Нахождение разницы между максимальным и минимальным ненулевым значением'
                       '\nдробной части элементов списка')

    n = common.get_user_input_int('\nВведите количество элементов списка: ',
                                  WARN_OUT_OF_RANGE, lambda a: a > 0)

    min_val = common.get_user_input_int_range(
        'Введите нижний предел диапазона значений списка: ')
    max_val = common.get_user_input_int_range(
        'Введите верхний предел диапазона значений списка: ', min_val)

    mode = common.get_user_input_int_range('\nЗадайте режим учёта знака числа (0/1)'
                                           '\n  0 \u2014 дробная часть не наследует знака,'
                                           '\n  1 \u2014 дробная часть имеет тот же знак, что и число'
                                           '\n?:', 0, 1)

    lst = create_list_random_float(n, min_val, max_val)
    (fmin, fmax) = get_fractional_nonzero_min_max(lst,
                                                  EPSILON,
                                                  DIGITS_PRECISION,
                                                  signed=mode == 1)
    delta = round(fmax - fmin, DIGITS_PRECISION)

    fmin_str = f'({fmin})' if fmin < 0 else str(fmin)
    fmax_str = f'({fmax})' if fmax < 0 else str(fmax)

    print('\nВывод', '(с учётом знака числа): ' if mode == 1
          else '(без учёта знака числа):')
    print(', '.join(map(lambda x: f'{x:g}', lst)), ' -> ', end='')
    print(common.console_format(f'{fmax_str} - {fmin_str} =', fore_color=ForeColor.BRIGHT_YELLOW),
          common.console_format(delta, bold=True, fore_color=ForeColor.BRIGHT_YELLOW))

    print()

    user_answer = common.ask_for_repeat()
