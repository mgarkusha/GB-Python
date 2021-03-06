# Задача-1:
# Дан список заполненный произвольными целыми числами, получите новый список элементами которого будут
# квадратные корни элементов исходного списка, но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
import math
spisok1 = [2, -5, 8, 9, -25, 25, 4, 0.25, -100000000000, 1000000]
spisok2 = []
for i in spisok1:
	if i >= 0:
		if (math.sqrt(i)).is_integer() == True:
			spisok2.append(int(math.sqrt(i)))
		else:
			continue
print(spisok2)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
print('\n')

days_1_19 = ['первое', 'второе', 'третье', 'четверное', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое', 'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнидцатое', 'шестнадцатое', 'семнадцатое', 'восемнадцатое', 'девятнадцатое']
days_20 = ['двадцатое']
days_30 = ['тридцатое']
days_20_30 = ['двадцать', 'тридцать']
month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

current_date = '31.08.2013'

day = int(current_date[0:2])
month = int(current_date[3:5])
year = current_date[6:]

current_date_string = []
if day <= 19:
	current_date_string.append(days_1_19[day-1])
elif day == 20:
	current_date_string.append(days_20[0])
elif day >= 21:
	if int(day / 10) == 2:
		current_date_string.append(days_20_30[0])
		i = day % 20
		current_date_string.append(days_1_19[i-1])
	elif int(day / 10) == 3:
		current_date_string.append(days_20_30[1])
		i = day % 30
		current_date_string.append(days_1_19[i-1])
current_date_string.append(month_list[month-1])
current_date_string.append(year)

date_out = ' '.join(current_date_string)

print(date_out, 'года')


# Задача-3: Напишите алгоритм заполняющий список произвольными целыми числами в диапазоне от -100 до 100
# В списке должно быть n - элементов
# Подсказка: для получения случайного числа изпользуйте функцию randint() модуля random
print('\n')
import random
my_spisok = []
i = 0
my_random = int(input('Введите число элементов списка: '))
while i <= my_random:
	my_spisok.append(random.randint(-100, 100))
	i += 1
print (my_spisok)

# Задача-4: Дан список заполненный произвольными целыми числами
# Получите новый список, элементами которого будут только уникальные элементы исходного
print('\n')
my_spisok_unikum = []

for i in my_spisok:
	if my_spisok_unikum.count(i) <= 0:
		my_spisok_unikum.append(i)
print(my_spisok_unikum)
no_unikum = len(my_spisok) - len(my_spisok_unikum)
print('\nКоличество не уникальных чисел = ', no_unikum)
