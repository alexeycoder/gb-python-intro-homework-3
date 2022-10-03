# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

import datetime
import math
import sys
import common


# consts:

WARN_OUT_OF_RANGE = 'Количество должно быть натуральным числом!'
WARN_OUT_OF_RANGE_DISTR = 'Для формирования выборки требуется более 10 чисел!'
DIAG_WIDTH = 50

# types:


class Randomizer:
    __RAW_MAX: int = 999999  # Макс величина микросекунд
    __RAW_DIGITS = len(str(__RAW_MAX))
    __FLOAT_EPSILON = sys.float_info.epsilon
    __ALMOST_ZERO = 100 * __FLOAT_EPSILON
    __ALMOST_ONE = 1.0 - __ALMOST_ZERO
    __DIVIDER_TO_NORMALIZE: float = __RAW_MAX + 1 - __FLOAT_EPSILON

    _prior_mcs = 1

    @staticmethod
    def __reverse_number(number):
        reversed_num = 0
        while number > 0:
            reversed_num = reversed_num * 10 + number % 10
            number //= 10
        return reversed_num

    def __summ_digits(number):
        sum = 0
        while number > 0:
            sum += number % 10
            number //= 10
        return sum

    @staticmethod
    def __trim_digits(value, num_of_digits):
        magnitude = 10**num_of_digits
        return value % magnitude

    @staticmethod
    def __get_random_raw():
        multiplier = Randomizer.__summ_digits(Randomizer._prior_mcs) * math.pi
        mcs = datetime.datetime.now().microsecond
        Randomizer._prior_mcs = mcs
        reversed = Randomizer.__reverse_number(mcs)
        reversed *= multiplier
        reversed = Randomizer.__trim_digits(reversed, Randomizer.__RAW_DIGITS)
        return reversed

    @staticmethod
    def get_random():
        normalized_value = Randomizer.__get_random_raw() / Randomizer.__DIVIDER_TO_NORMALIZE
        if normalized_value < Randomizer.__ALMOST_ZERO:
            return float(0)
        elif normalized_value > Randomizer.__ALMOST_ONE:
            return float(1)
        return normalized_value

    @staticmethod
    def get_random_range_float(min_value, max_value):
        if (max_value < min_value):
            min_value, max_value = max_value, min_value
        rnd_value = Randomizer.get_random()
        return min_value + (max_value - min_value) * rnd_value

    @staticmethod
    def get_random_range_int(min_value, max_value):
        return int(round(Randomizer.get_random_range_float(min_value, max_value)))


# methods:

def get_distribution_dict(values_list, step, max_value):
    distribution_dict = {i: 0 for i in range(step, max_value + 1, step)}
    for rnd_value in values_list:
        for top_value, count in distribution_dict.items():
            if rnd_value < top_value and rnd_value >= top_value - step:
                distribution_dict[top_value] = count + 1
    return distribution_dict


def print_distribution(distr_dict: dict, diagram_width, symbol):
    num_of_ranges = len(distr_dict)
    if num_of_ranges == 0:
        return

    counts = list(distr_dict.values())
    max_count = max(counts)
    sum_count = sum(counts)
    top_values = list(distr_dict.keys())
    step = top_values[num_of_ranges-1] - top_values[num_of_ranges-2]

    def get_legend(range_top_value):
        return f'от {range_top_value-step} до {range_top_value}: '

    padding = 2
    max_legend_len = padding + len(get_legend(top_values[num_of_ranges-1]))

    def get_width(range_count):
        return int(round(diagram_width * range_count / max_count))

    header_count = f'Кол-во попаданий в интервал (макс={max_count}, всего={sum_count})'
    header_legend = 'Интервал [от,до)'
    max_legend_len = max(max_legend_len, len(header_legend)+2)
    header_legend = header_legend.ljust(max_legend_len)

    header_legend = common.console_format(header_legend, bold=True)
    header_count = common.console_format(header_count, bold=True)

    print(header_legend, '|', header_count, sep='')

    for top_value, count in distr_dict.items():
        print(get_legend(top_value).ljust(max_legend_len),
              '|', symbol*get_width(count), sep='')


# main flow:

user_answer = True

while(user_answer):
    common.console_clear()
    common.print_title('Реализация генератора псевдослучайных чисел')

    n = common.get_user_input_int('\nЗадайте количество сгенерированных чисел для демонтрации: ',
                                  WARN_OUT_OF_RANGE, lambda a: a > 0)

    min_val = common.get_user_input_int_range('Задайте минимальное значение: ')
    max_val = common.get_user_input_int_range('Задайте максимальное значение: ',
                                              min_val)

    print(common.console_format(
        '\nПсевдослучайные целые числа:\n', bold=True, italic=True))

    for i in range(n):
        print(Randomizer.get_random_range_int(min_val, max_val), end='  ')

    print()
    print(common.console_format(
        '\nПсевдослучайные вещественные числа:\n', bold=True, italic=True))

    for i in range(n):
        print(Randomizer.get_random_range_float(min_val, max_val), end='  ')

    print()
    print('\nДля анализа работы генератора псевдослучайных чисел'
          '\nпостроим диаграмму распределения сгенерированных'
          '\nвещественных чисел в диапазоне от 0 до 100 с шагом 10.')

    n = common.get_user_input_int('\nЗадайте количество сэмплов выборки (>10): ',
                                  WARN_OUT_OF_RANGE_DISTR, lambda a: a > 10)

    demo_max = 100
    demo_step = 10
    lst_of_randoms = [Randomizer.get_random_range_float(0, demo_max)
                      for _ in range(n)]
    distr = get_distribution_dict(lst_of_randoms, demo_step, demo_max)

    print(common.console_format(
        '\nДиаграмма распределения:\n', bold=True, italic=True))
    print_distribution(distr, 30, '\u25a9')

    print()

    user_answer = common.ask_for_repeat()
