"""Напишите функцию-генератор all_variants(text),
которая принимает строку text и возвращает объект-генератор, при каждой итерации которого
будет возвращаться подпоследовательности переданной строки.
Пункты задачи:
-Напишите функцию-генератор all_variants(text).
-Опишите логику работы внутри функции all_variants.
-Вызовите функцию all_variants и выполните итерации"""

def all_variants(text):
    l = len(text) # вычисляем длину строки
    for x in range(l + 1):
        for y in range(l - x + 1):
            yield text[y: x + y]

a = all_variants("abc")
for i in a:
    print(i)




