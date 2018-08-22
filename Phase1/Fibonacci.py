
""" Below function generates Fibonacci numbers """


def generate_fibonacci(length):
    a = 0
    b = 1
    fib = [a, b]
    if length >= 0:
        for i in range(0, length):
            c = a + b
            a = b
            b = c
            fib.append(c)
        print(fib)
    else:
        print('Your argument must be bigger then 0!')


generate_fibonacci(10)
