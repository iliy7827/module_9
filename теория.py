''' Списковые, словарные сборки '''
from curses import start_color

from main import print_hi


# пример 1 - как выглядит объединение функций map и filter

def by_3(x): # функция для операции над элементом
    return x * 3

def is_odd(x): # функция для фильтрации
    return x % 2
my_numbers = [3,1,4,1,5,9,2,6]
result = map(by_3, filter(is_odd, my_numbers))
print(list(result))

# пример 2 - списковая сборка - это аналог функции map
my_numbers = [3,1,4,1,5,9,2,6]
result = [x * 3 for x in my_numbers] # циклом фор перебираем список и уиножаем каждый элемент на 3
print(result)

# пример 3 - списковая сборка с if - это аналог функции filter
my_numbers = [3,1,4,1,5,9,2,6]
result = [x * 3 for x in my_numbers if x % 2]
# циклом фор перебираем список и умножаем каждый элемент на 3 если остаток от деления на 2 будет больше нуля. только нечетные числа
print(result)

# пример 4 - условия перед циклом(для того чтобы не отфильтровывать данные, а поменять операцию над ними)
my_numbers = ['A',1,4,'B',5,'C',2,6]
result = [x if type(x) == str else x*5 for x in my_numbers]
# добавляем Х если его тип = str, иначе добавляю x*5
print(result)

# пример 5 - можно делать вложенные циклы
my_numbers = [3,1,4,1,5,9,2,6]
they_numbers = [2,7,1,8,2,8,1,8]

result = [x * y for x in my_numbers for y in they_numbers]
print(result)

result = [x * y for x in my_numbers for y in they_numbers if x % 2]
print(result)

result = [x * y for x in my_numbers for y in they_numbers if x % 2 and y // 2]
print(result)

# пример 6 - можно создавать на лету множества и словари
my_numbers = [3,1,4,1,5,9,2,6]
result = {x for x in my_numbers} # ставим фигурные скобки и будет множество - упорядоченая коллекция данных
print(result)

they_numbers = [2,7,1,8,2,8,1,8]
result = {x: x ** 2 for x in they_numbers}
print(result)

'''Генераторная сборка'''
# пример 7 - ленивые вычисления - это когда значения вычисляются при необходимости(а не сразу, когда мы записываем)
# Это делают генераторы
my_numbers = [3,1,4,1,5,9,2,6]
result = (x ** 100 for x in my_numbers)
#print(result)

for elem in result:
    print(elem)

# пример 8 - прочитать генераторную сборку можно лиш один раз
my_numbers = [3,1,4,1,5,9,2,6]
result = (x ** 1000 for x in my_numbers)
for elem in result:
    print(elem)
print("еще разок")
for elem in result: # второй раз не вызывается
    print(elem)

# пример 9 - Генератор используется там где надо производить затратные операции
import time

start_time = time.time() # время начала выполнения программы
my_numbers = [3,1,4,1,5,9,2,6]
#result = (x ** 3000 for x in my_numbers) - списковая сборка
result = (x ** 3000 for x in my_numbers) # генераторная сборка
print(result)

for i in result:
    print(i)

finish_time = time.time() # время окончания выполнения программы
print(f'время в миллисекундах: {(finish_time - start_time) * 1000}')

# пример 10 - Демонстрация встроенных функций  ленивыми вычислениями
list_1 = [1, 5, 9, 29, 4]
list_2 = [5, 2, 9, 1, 2]

ran = range (10, 30) #это встроенная функция, которая возвращает итерируемый объект, содержащий целые числа. С её помощью можно сгенерировать последовательность чисел
zp = zip(list_1, list_2) # попарно объединяет элементы из 2 списков - создает из них кортежи
mp = map(str, list_1) # перевести в строку. Позволяет связать элемент с операцией, которую нужно выполнить

print(ran, zp, mp)

print(list(ran))
print(list(zp))
print(list(mp))