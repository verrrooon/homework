
print("Стандартное квадратное уравнение имеет вид ax^2+bx+c = 0 ")
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
d = b ** 2 - 4 * a * c
if d < 0:
    print("Корней нет!")
    exit()
elif d == 0:
    print("x = ", (-b / (2 * a)))
elif d > 0:
    print("x1 = ", float((-b + d**0.5) / (2 * a)))
    print("x2 = ", float((-b - d**0.5) / (2 * a)))