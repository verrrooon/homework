try:
    f = open('homework6/Ex-2/input.txt', 'r')
    lst = list(f)
    lst = lst[0].split()
    rez = min(int(lst[0])//2, int(lst[1])//6, int(lst[2]))
    output = open('homework6/Ex-2/output.txt', 'w')
    output.write(f'Максимально возможное число молекул спирта: {rez}')
    f.close()
    output.close()
except FileNotFoundError:
    print('Файл не найден')
