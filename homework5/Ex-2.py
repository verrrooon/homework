def add(*args):
    """функция для сложения с любым количеством аргументов"""
    sum = 0
    for i in args:
        sum += i

    print('Сумма =', sum)
