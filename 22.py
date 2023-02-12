# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.


def get_number():
    return int(input('Введите число: '))


def get_list(list_length):
    print('Элементы списка')
    new_list = [get_number() for i in range(list_length)]
    print(new_list)
    return new_list


def get_two_lists_duplicates(list1, list2):
    return sorted(set(list1).intersection(set(list2)))


print(get_two_lists_duplicates(get_list(get_number()), get_list(get_number())))
