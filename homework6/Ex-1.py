
a = input('Введите cписок строк: ').split()


def straight(a):
    for i in range(len(a)):
        a[i] = a[i].encode('utf-8')
    return a


def back(a):
    for i in range(len(a)):
        a[i] = a[i].decode('utf-8')
    return a


print(f'Прямое преобразование: {straight(a)}')
print(f'Обратное преобразование:{back(a)}')
