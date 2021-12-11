"""программа для вычисления конечных координат с незаданным количеством повторений"""
print("Для остановки введите стоп")
stop = 0
check = ["влево", "вправо", "вверх", "вниз"]
"""координаты, с которых начинается отсчет"""
coordinates = [0, 0]
while stop == 0:

    direction = input("Введите направление: влево, вправо, вверх, вниз \n")

    if direction == "стоп":
        stop = 1

    if direction not in check:
        print("Введите корректное направление!")

    else:
        quantity = float(input("Введите число шагов \n"))

        if quantity < 0:
            print("Количество шагов не может быть отрицательным!")

        else:

            if direction == "влево":
                coordinates[0] = coordinates[0] - quantity

            elif direction == "вправо":
                coordinates[0] = coordinates[0] + quantity

            elif direction == "вверх":
                coordinates[1] = coordinates[1] + quantity

            elif direction == "вниз":
                coordinates[1] = coordinates[1] - quantity

print("Конечные координаты =", coordinates)
