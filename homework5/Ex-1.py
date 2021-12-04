code = input('Введите пароль: ')
def check(a):
    if (len(a) < 6) or (not any([x in a for x in '0123456789'])) or (a.isdigit()) or ('password' in a.lower()):
        return False
    else:
        return True
if check(code) == True:
    print ('Пароль верен')
if check(code) == False:
    print ('Пароль неверен')