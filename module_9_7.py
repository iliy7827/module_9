"""Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое",
если результат 1ой функции будет простым числом и "Составное" в противном случае."""

def is_prime(func):
    def wrapper(*args, **kwargs):
        summ = func(*args, **kwargs)
        x = 0
        for i in range(2, int(summ ** 0.5) + 1):
                if summ % i == 0:
                    x = x + 1
        if x <= 0:
            print('Простое')
        else:
            print('Составное')
        return summ
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6,)
print(result)


