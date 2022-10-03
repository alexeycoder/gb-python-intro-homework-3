# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

import common
from common import ForeColor

# consts:

WARN_OUT_OF_RANGE = 'Ошибка: Требуется неотрицательное целое число! ' + \
    common.PLEASE_REPEAT


# methods:

def get_pseudo_binary(decimal_number):
    result = 0
    i = 1
    while decimal_number > 0:
        result += (decimal_number % 2)*i
        decimal_number //= 2
        i *= 10
    return result


# main flow:
user_answer = True

while(user_answer):
    common.console_clear()
    common.print_title('Преобразование десятичного числ в двоичное')

    dec_num = common.get_user_input_int('\nВведите неотрицательное десятичное целое число: ',
                                        WARN_OUT_OF_RANGE, lambda a: a >= 0)
    bin_num = get_pseudo_binary(dec_num)

    print(f'\n{dec_num} ->', common.console_format(bin_num,
          bold=True, fore_color=ForeColor.BRIGHT_YELLOW))
    print()

    user_answer = common.ask_for_repeat()
