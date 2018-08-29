
""" Below function generates Fibonacci numbers """


def main():
    print(list(generate_fibonacci(10)))
    print(list(test(10)))


def generate_fibonacci(length):
    a = 0
    b = 1
    fib = [a, b]
    if length >= 0:
        for i in range(length):
            c = a + b
            a = b
            b = c
            fib.append(c)
        return fib
    else:
        return False


if __name__ == '__main__':
    main()


