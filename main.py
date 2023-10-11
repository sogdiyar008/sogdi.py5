#Ряд - 1
# A=int(input())
# B=int(input())
# for i in range (A, B+1):
# 	print(i)


# Ряд - 2
# a=int(input())
# b=int(input())
# if a<b:
# 	for i in range (a, b+1):
# 		print(i)
# elif a>b:
# 	for i in range (a, b-1, -1):
# 		print(i)


# Сумма N чисел
# a = [int(input('какие числа нужно суммировать?:  ')) for i in range(int(input('колво раз цифр каоторые нужно суммировать: ')))]
# print(" сумма: ", sum(a),'\n', 'наименьшее число переменных нужно для решения этой задачи: 1')


# Факториал
# factorial=int(input('факториал какого числа ваам нужно?:  '))
# for i in range (1, factorial):
# 	factorial = factorial*i
# print (factorial)


# Лесенка
# n=int(input('какую леченку пожелаешь?(до 9):  '))
# if n<=9:
# 	for i in range(1, n+1):
# 		for j in range(1, i+1):
# 			print(j, end='')
# 		print()
# else:
# 	print("число больше 9!!!!!!")


##############################################################################################################


# Список квадратов
# kv = int(input('до какого числа вывести квадраты?:  '))
# for i in range (1, kv+1):
# 	print(i ** 2)

# Степень двойки
# power_of_two=int(input('введите число N:  '))
# power = 0
# result=1
# while result<=power_of_two:
# 	power+=1
# 	result*=2
# print('наибольший показатель степени: ', power-1, 'которое равно: ',result//2 )


# Утренняя пробежка
# x=int(input())
# y=int(input())
# days=0
# while x<=y:
# 	days+=1
# 	x=x+x/10
# print(days)


# Задача «Длина последовательности»
# numbers = 0
# while int(input('введите числа:  ')) != 0:
#     numbers += 1
# print(numbers)


# Количество элементов, которые больше предыдущего
# firs_number = int(input('первая число:  '))
# quantity = 0
# while firs_number != 0:
#     next = int(input('введите следующие числа:  '))
#     if next != 0 and firs_number < next:
#         quantity += 1
#     firs_number = next
# print(quantity)

# Второй максимум
# first_max = int(input('находит второй максимум, чисел которые вы введете:  '))
# second_max = int(input('находит второй максимум, чисел которые вы введете:  '))
# if first_max < second_max:
#     first_max, second_max = second_max, first_max
# helper_element = int(input('находит второй максимум, чисел которые вы введете:  '))
# while helper_element != 0:
#     if helper_element > first_max:
#         second_max, first_max = first_max, helper_element
#     elif helper_element > second_max:
#         second_max = helper_element
#     helper_element = int(input('находит второй максимум, чисел которые вы введете:  '))
# print(second_max)

# Числа Фибоначчи
# уже ведь рещалии((
# number_of_Finobacci=int(input('номер числа Фибоначчи:  '))
# fib1 = fib2 = 1
# number_of_Finobacci = number_of_Finobacci - 2
# for i in range (number_of_Finobacci):
#     fib1, fib2 = fib2, fib1 + fib2
# print(f"Значение этого элемента: {fib2}")


# Максимальное число идущих подряд равных элементов


# Четные индексы
# numbers = input('введи текст, и я покажу как он будет выглядеть, пиши ты его через букву:  ')
# for i in range(0, len(numbers), 2):
#     print(numbers[i])

# Больше предыдущего
# a = [int(a) for a in input("введи числа через пробел. я покажу какие из них больше пред.:  ").split()]
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i])

# Наибольший элемент
# index_of_max = 0
# a = [int(i) for i in input("введи числа через пробел. я покажу индекс и само большое число:  ").split()]
# for i in range(1, len(a)):
#     if a[i] > a[index_of_max]:
#         index_of_max = i
# print('само большое число: ',a[index_of_max], ',  и его индекс: ',index_of_max)


# Шеренга
# a = [int(i) for i in input('рост остальных, введи чрез пробел:  ').split()]
# x = int(input('рост пети:  '))
# pos = 0
# while pos < len(a) and a[pos] >= x:
#     pos += 1
# print(pos + 1)


# Вставить элемент
# a = [int(s) for s in input('введи список чисел через робел:  ').split()]
# k, C = [int(s) for s in input('введи К(куда нужно поставить)  и С(что нужно вствать):  ').split()]
#
# a.append(0)
# for i in range(len(a) - 1, k, -1):
#     a[i] = a[i - 1]
# a[k] = C
# print(' '.join([str(i) for i in a]))

# Ферзи
# n = 8
# x = []
# y = []
# for i in range(n):
#     new_x, new_y = [int(s) for s in input('новый X и Y:  ').split()]
#     x.append(new_x)
#     y.append(new_y)
#
# correct = True
# for i in range(n):
#     for j in range(i + 1, n):
#         if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
#             correct = False
#
# if correct:
#     print('NO')
# else:
#     print('YES')