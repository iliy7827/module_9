"""Необходимо создать 2 генераторных сборки:"""

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# запишем в переменную разницу длин из списков first и second если их длины не равны
first_result = (len(x) - len(y) for x, y in zip(first,second) if len(x) != len(y))
# запишем в переменную сравнения длин строк в одинаковых позициях из списков first и second
second_result = (len(first[x]) == len(second[x]) for x in range(min(len(first), len(second))))

print(list(first_result))
print(list(second_result))


