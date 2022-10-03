# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import common
import random
from common import ForeColor

# consts:

WARN_OUT_OF_RANGE = 'Ошибка: Количетсво элементов не может быть меньше одного! ' + \
    common.PLEASE_REPEAT


# methods:

def create_list_random_int(length, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(length)]


def get_sum_by_odd_positions(numbers_list):
    return sum(numbers_list[0::2])


# def get_sum_by_odd_positions_ver2(numbers_list):
#     sum_odd_pos = 0
#     for position in range(1, len(numbers_list) + 1, 2):
#         sum_odd_pos += numbers_list[position - 1]
#     return sum_odd_pos


def set_gray(text):
    return common.console_format(text, fore_color=ForeColor.GRAY)


def set_bright(text):
    return common.console_format(text, bold=True, fore_color=ForeColor.BRIGHT_WHITE)


def get_formatted_list_as_str(numbers_list):
    arrow_sign = '\u21E8'
    def to_position_str(index): return set_gray(str(index+1)+arrow_sign)
    str_list = [
        f'{to_position_str(idx)}{set_bright(val) if (idx+1)%2!=0 else val}' for idx, val in enumerate(numbers_list)]
    return ', '.join(str_list)


# main flow:

user_answer = True

while(user_answer):
    common.console_clear()
    common.print_title('Сумма элементов списка, стоящих на нечётных позициях'
                       '\n(подразумевается, что отсчёт позиций начинается с 1, не с 0!)')

    n = common.get_user_input_int('Введите количество элементов списка: ',
                                  WARN_OUT_OF_RANGE, lambda a: a > 0)

    min_val = common.get_user_input_int_range(
        'Введите нижний предел диапазона значений списка: ')
    max_val = common.get_user_input_int_range(
        'Введите верхний предел диапазона значений списка: ', min_val)

    lst = create_list_random_int(n, min_val, max_val)

    sum_val = get_sum_by_odd_positions(lst)

    print('\nСформированный список: ', lst)
    print('Позиция\u21E8Значение: ', get_formatted_list_as_str(lst))
    print('Сумма чисел на нечётных позициях =',
          common.console_format(sum_val, bold=True, fore_color=ForeColor.BRIGHT_YELLOW))
    print()

    user_answer = common.ask_for_repeat()
