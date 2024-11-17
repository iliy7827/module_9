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


