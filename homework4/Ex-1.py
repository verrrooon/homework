from random import randint

a = [randint(0, 35) for _ in range(50)]
print('До сортировки:', a)

for i in range(len(a)):
    for j in range(len(a) - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print('После сортировки:', a)