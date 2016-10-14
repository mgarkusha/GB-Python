# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    my_list = [1, 1]
    i = 2
    while i < m:
        my_list.append(my_list[i - 1] + my_list[i - 2])
        i += 1
    return print(my_list)


fibonacci(1, 10)


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    for i in origin_list:
        j = 0
        while j < (len(origin_list) - 1):
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
            j += 1
    return print(origin_list)


sort_to_max([10, 2, 1, -1.6, 40, 5])


# Задача-3:
# Напишите собственную реализацию функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_filter(numbers, number, condition):
    new_numbers = []
    for i in numbers:
        if condition == '>':
            if i > number:
                new_numbers.append(i)
        elif condition == '<':
            if i < number:
                new_numbers.append(i)
        elif condition == '=':
            if i == number:
                new_numbers.append(i)
    return print(new_numbers)


numbers = [1, 2, 4, 5, 5, 10, 20]
my_filter(numbers, 5, '=')

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
