"""Игра угадайка число
"""
    
import numpy as np
from numpy.lib.function_base import average

#Функция загадывания числа
def number_think(max_num):
    return np.random.randint(1, max_num+1)


def numb_divine(max_num, thnk_numb):
    my_numb = np.random.randint(1, max_num+1)
    max_border = max_num+1
    min_border = 1
    count = 1
    
    while True:
        if my_numb > thnk_numb:
            max_border = my_numb
            my_numb = np.random.randint(min_border, max_border)
            
        elif my_numb < thnk_numb:
            min_border = my_numb
            my_numb = np.random.randint(min_border, max_border)
            
        else:
            return count
        count += 1
        my_numb = np.random.randint(min_border, max_border)


def mean_counts(max_num):
    mean_arr = []
    for i in range(max_num):
        thnk_numb = number_think(max_num)
        count = numb_divine(max_num, thnk_numb)
        mean_arr.append(count)
    return np.average(mean_arr)



if __name__ == '__main__':
    max_num = input('Введите максимальное целое число: ')

    try:
        max_num = int(max_num)
    except ValueError:
        max_num = input('Ошибка ввода. Введите максимальное целое число: ')

    print(mean_counts(max_num))