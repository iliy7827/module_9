def apply_all_func(int_list, *functions):
    '''Эта функция должна:
-Вызвать каждую функцию к переданному списку int_list
-Возвращать словарь, где ключом будет название вызванной функции,
а значением - её результат работы со списком int_list.'''
    results = {} # создаем словарь
    for func in functions: #При переборе функций записать в словарь results результат работы этой функции под ключом её названия.
        results[func.__name__] = func(int_list)  #чтобы взять название функции можно обратиться к атрибуту __name__
    return results  #возвращаем словарь

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))