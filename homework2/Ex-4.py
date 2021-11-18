import math
print("Введите радиус круга")
r=float(input())
if r<=0:
    print("Радиус должен быть положительным!")
else:
    print("Площадь круга =", (math.pi*(r**2)))