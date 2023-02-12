# Задача 24
from random import randint


def get_number():
    return int(input('Введите число: '))


def get_list(list_length):
    new_list = [randint(1, 10) for i in range(list_length)]
    print(new_list)
    return new_list


def get_list_of_values(new_list):
    list_of_sums = [new_list[i-1] + new_list[i] + new_list[i+1] for i in range(len(new_list) - 1)]
    list_of_sums.append(new_list[0] + new_list[-1] + new_list[-2])
    return list_of_sums


print(max(get_list_of_values(get_list(get_number()))))
