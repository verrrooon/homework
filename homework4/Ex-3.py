from random import randint

a = {randint(0, 15) for _ in range(15)}
b = {randint(0, 15) for _ in range(15)}
"""создание строки a из 15 чисел
создание строки b из 15 чисел
"""
print('Первое множество', a)
print('Второе множество', b)
print('входят одновременно в оба ', a & b)
print('входят только в первое, но не входят во второе; ', a.difference(b))
print('входят только во второе, но не входят в первое; ', b.difference(a))
print('входят в первое или во второе, но не в оба из них одновременно; ',
      a.symmetric_difference(b))
