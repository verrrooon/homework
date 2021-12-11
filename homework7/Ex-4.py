import os
print('Имя операционной системы = ', os.name)
print('Имя пользователя, вошедшего в терминал = ', os.getlogin())
print('Список файлов и директорий в папке = ', os.listdir(path="."))
