def fib(a):
    if a in [1, 2]:
        return 1
    return fib(a - 1) + fib(a - 2)
