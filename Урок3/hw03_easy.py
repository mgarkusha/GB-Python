# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math

#Кажется, моё решение через строки было в корне неправильным??? :) пока бросил, подскажите пожалуйста как решать
def my_round(number, ndigits):
	big_number = str(number * 10 ** (ndigits + 1)) # + 1 что-бы с точкой не встречаться
	print(big_number)
	print(big_number[ndigits + 1:ndigits + 2])
	print(big_number[:ndigits + 1])
	if int(big_number[ndigits + 1:ndigits + 2]) >= 5:
		new_big_number = int(big_number[:ndigits + 1]) + 1
	else:
		new_big_number = int(big_number[:ndigits + 1])
	out_number = new_big_number / 10 ** (ndigits)
	print(out_number)

my_round(22.2757, 3)

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
print('\n')


def lucky_ticket(ticket_number):
	'''
	Фнукия сработает если билет счастливый
	'''
	lucky = 0
	summ_one_hulf = 0
	summ_two_hulf = 0
	one_hulf = str(ticket_number)[:3]
	two_hulf = str(ticket_number)[3:]
	for number_one_hulf in one_hulf:
		summ_one_hulf += int(number_one_hulf)
	for number_two_hulf in two_hulf:
		summ_two_hulf += int(number_two_hulf)
	if summ_one_hulf == summ_two_hulf:
		lucky += 1
	return lucky
		
ticket = int(input('Введите 6-ти значный номер билета: '))

if (lucky_ticket(ticket)):
	print('Ваш билет счастливый!!!')
else:
	print('Не счастливый')