"""УСЛОВИЯ ЗАДАНИЯ.

1. Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать» подразумевается «написать программу, которая угадывает число».
2. Алгоритм учитывает информацию о том, больше ли или меньше случайное число нужного нам числа.

МЕТРИКА КАЧЕСТВА

1. Результаты оцениваются по среднему количеству попыток при 1000 повторений. Необходимо добиться минимального количества попыток.
"""


import numpy as np


def think_number(up_border: int = 100) -> int:
    """Функция загадывает целое число от 1 до верхней границы.

    Args:
        up_border (int, optional): Верхнияя граница даипозона загадывания. Defaults to 100.

    Raises:
        ValueError: Возвращает ошибку, если записано неверное число

    Returns:
        int: Возвращает загаданное число.
    """

    if (type(up_border) is int) and (up_border > 10):  # Проверим на корректность ввод границы
        return np.random.randint(1, up_border + 1)

    else:
        raise ValueError('Invalid border type. It must be integer!')


def number_guess(thnk_num: int, up_border: int = 100, ptr_text: bool = True) -> int:
    """Функция угадывания числа.

    Args:
        thnk_num (int): Загаданное число
        up_border (int, optional): Верхняя граница угадывания. Defaults to 100.

    Returns:
        int: Возвращает количество попыток, за которое угадано число.
    """
    # Зададим начальные параметры и сделаем первую попытку
    count = 1  # Число попыток
    min_num = 1  # Нижняя граница угадывания
    max_num = up_border + 1  # Верхняя граница угадывания
    guess_num = np.random.randint(min_num, max_num)  # Делаем первую попытку

    while True:  # Цикл угадывания со смещением верхней и нижней границы

        if guess_num < thnk_num:
            min_num = guess_num

        elif guess_num > thnk_num:
            max_num = guess_num

        else:
            if ptr_text:  # Проверка нужно ли печатать результаты
                print(f'Число {thnk_num} угадано за {count} попыток.')

            return count

        count += 1
        guess_num = np.random.randint(min_num, max_num)


def mean_score(up_border: int = 100, prt_text: bool = True) -> int:
    """Функция считает число попыток 1000 раз и возвращает среднее число
    попыток.

    Args:
        up_border (int, optional): Верхняя граница даипозона угадывания. Defaults to 100.
        prt_text (bool, optional): Опция печати или не печати сообщения о среднем количестве попыток. Defaults to True.

    Returns:
        int: Возвращает среденее число попыток из 1000 игр.
    """

    count_ls = []  # Задаем начальное значение списка попыток

    for i in range(999):  # Делаем все 1000 попыток
        count_ls.append(number_guess(
            think_number(up_border), up_border, False))

    score = int(np.mean(count_ls))  # Считаем результаты

    if prt_text:  # Проверка нужно ли печатать результаты
        print(
            f'Среднее число попыток для даипозона от 1 до {up_border} - {score}.')

    return score


if __name__ == '__main__':
    # RUN
    print(mean_score(50001, False))
    mean_score()
    mean_score(1000)
    print(mean_score(1000, False))
