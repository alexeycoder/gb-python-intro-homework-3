# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import common
import random
from common import ForeColor

# consts:

WARN_OUT_OF_RANGE = 'Ошибка: Количетсво элементов не может быть меньше одного! ' + \
    common.PLEASE_REPEAT


# methods:

def get_first_last_product_list(numbers_list):
    length = len(numbers_list)
    half_num = length//2 if length % 2 == 0 else length//2 + 1
    return [first * last for (first, last) in zip(numbers_list[0:half_num], numbers_list[::-1][0:half_num])]


def create_list_random_int(length, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(length)]


# main flow:

user_answer = True

while(user_answer):
    common.console_clear()
    common.print_title(
        'Произведения пар чисел списка, первого с последним, второго с предпоследним и т.д.')

    print(common.console_format(
        '\nВариант со сгенерированным списком:\n', True, True))

    n = common.get_user_input_int('Введите количество элементов списка: ',
                                  WARN_OUT_OF_RANGE, lambda a: a > 0)

    min_val = common.get_user_input_int_range(
        'Введите нижний предел диапазона значений списка: ')
    max_val = common.get_user_input_int_range(
        'Введите верхний предел диапазона значений списка: ', min_val)

    lst = create_list_random_int(n, min_val, max_val)

    prods = get_first_last_product_list(lst)

    print('\n', lst, '=>',
          common.console_format(prods, fore_color=ForeColor.BRIGHT_WHITE), sep='  ')

    print(common.console_format(
        '\nВариант с контрольными списками:\n', True, True))

    lst_a = [2, 3, 4, 5, 6]
    lst_b = [2, 3, 5, 6]

    prods_a = get_first_last_product_list(lst_a)
    prods_b = get_first_last_product_list(lst_b)

    print('', lst_a, '=>',
          common.console_format(prods_a, fore_color=ForeColor.BRIGHT_WHITE), sep='  ')
    print('', lst_b, '=>',
          common.console_format(prods_b, fore_color=ForeColor.BRIGHT_WHITE), sep='  ')
    print()

    user_answer = common.ask_for_repeat()
