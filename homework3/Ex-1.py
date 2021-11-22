direction = input("Введите направление: влево, вправо, вверх, вниз \n" )
check = ["влево","вправо","вверх","вниз"]
if direction not in check:
    print("Введите корректное направление!")
else: 
    quantity = float(input("Введите число шагов \n"))
    
    if  quantity < 0 :
        print("Количество шагов не может быть отрицательным!")
    else:
        
        coordinates = [0,0]
        if direction == "влево":
            coordinates[0] = 0 - quantity
            print("Конечные координаты =", coordinates)
        elif direction == "вправо":
            coordinates[0] = 0 + quantity
            print("Конечные координаты =", coordinates)
        elif direction == "вверх":
            coordinates[1] = 0 + quantity
            print("Конечные координаты =", coordinates)
        elif direction == "вниз":
            coordinates[1] = 0 - quantity
            print("Конечные координаты =", coordinates)
