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

"""Генераторная сборка"""
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

"""Создание функций на лету"""
#Когда нам нужны простые одноразовые функции, для которых def слишком жирно.
# Для этого есть lambda
# Пример 1 lambda - функции

my_func = lambda x: x + 10
print(my_func(x=42))
print(type(my_func))

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result = map(lambda x: x + 10, my_numbers)
print(list(result))

# Пример 2 lambda - форма может принимать как несколько параметров так и не одного

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]

result = map(lambda x, y: x + y, my_numbers, they_numbers)
print(list(result))
# lambda - форма функции имеет неограниченное применение:
# - Она создается в процессе выполнения кода (а не при компиляции) и может просадить быстродействие
# - Она плохо сериализуется - могут быть проблемы в крупных фреймворках
# - Не пытайтесь записать в lambda сложное выражение: если там более 3-5 операторов - пора сделать def

# Пример 3 Создание функции на лету
def get_multiplier_v1(n): #функц высщего порядка которая возвращает функции, хоть и не принимает в кач-ве аргументов себе другие функции
    if n == 2: #если n == 2 то тогда мы создаем
        def mulriplier(x): # функцию mulriplier с аргументом Х на входе
            return x * 2  # и возвращает x * 2

    elif n == 3: #если n == 3 то вызовется
        def mulriplier(x): #функция mulriplier
            return x * 3  # и вернет  x * 3

    else: # если введутся другие значения то выведем исключение только 2 или 3
        raise Exception('Я могу сделать умножители только на 2 или 3!')

    return mulriplier # вернем функцию mulriplier
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

by_2 = get_multiplier_v1 (2) #в переменну сохраняем результат функции get_multiplier_v1
by_3 = get_multiplier_v1 (3)

result = map(by_2, my_numbers)
print(list(result))
result = map(by_3, my_numbers)
print(list(result))

# Пример 4 Создание функции на лету замыкание

def get_multiplier_v2(n):
    def mulriplier(x):
        return x * n
    return mulriplier

by_5 = get_multiplier_v2(5)
print(by_5(x=42))

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

by_10 = get_multiplier_v2(10)
by_100 = get_multiplier_v2(100)

print(list(map(by_10, my_numbers)))
print(list(map(by_100, my_numbers)))

# Пример 6 Создание объекта который можно вызвать
class Multiplier:

    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        #если есть такой метод у класса - то его объект можно "вызывать" как функцию
        return x * self.n

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
by_100500 = Multiplier(n=100500)
result = by_100500(x=42)
print(result)

result = map(by_100500, my_numbers)
print(list(result))

""" Итераторы """
#Пример 1 библиотека itertools
import sys
from itertools import repeat

# Что же это за зверь такой - итератор?
#
# В python можно проходить циклом по любому обьекту, если он - итерируемый.
# А что бы обьект стал итерируемым, он должен содержать два метода - __iter__ и __next__

class Family:

    def __init__(self):
        self.dad = 'Вадим'
        self.mom = 'Татьяна'
        self.son = 'Алексей'
        self.i = 0

    def __iter__(self):
        # обнуляем счетчик перед циклом
        self.i = 0
        # возвращаем ссылку на себя - я буду итератором!
        return self

    def __next__(self):
        # а этот метод возвращает значения по требованию python
        self.i += 1
        if self.i == 1:
            return f'Папа - {self.dad}'
        if self.i == 2:
            return f'Мама - {self.mom}'
        if self.i == 3:
            return f'Я - {self.son}'
        if self.i == 4:
            return f'Счастливая семья :)'
        raise StopIteration()  # признак того, что больше возвращать нечего


my_family = Family()
print(my_family)
for value in my_family:
    print(value)

# То есть интерпретатор вызывает метод __next__ при каждом проходе цикла
# а если в __next__ возникает исключение StopIteration - то значит в обьекте нет больше элементов
# и цикл прекращается

# То есть под капотом у for происходит _как_бы_ следующее
try:
    while True:
        value = my_family.__next__()
        print(value)
except StopIteration:
    pass

# Такой же алгоритм срабатывает при вычислении вхождения в последовательность - оператор in
print('Я - Алексей' in my_family)


# Еще пример: последовательность Фибоначчи - https://goo.gl/PoqS7
# Последовательность, в которой каждое последующее число равно сумме двух предыдущих чисел:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, ...
def fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


for value in fibonacci(n=10):
    print(value)
# Для больших N функция создаст в памяти огромный список и вернет его - нерационально!


# Сделаем итератор, который будет вычислять следующее значение по требованию (lazy evaluation https://goo.gl/7fzXuA)
class Fibonacci:
    """Итератор последовательности Фибоначчи до N элементов"""

    def __init__(self, n):
        self.i, self.a, self.b, self.n = 0, 0, 1, n

    def __iter__(self):
        self.i, self.a, self.b = 0, 0, 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b
        return self.a


fib_iterator = Fibonacci(10)
print(fib_iterator)
for value in fib_iterator:
    print(value)
print(13 in fib_iterator)
# Каждое значение вычисляется "по месту" - тогда, когда оно понадобилось.
