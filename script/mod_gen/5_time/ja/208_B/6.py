def calc(n):
    if n == 0:
        return 0
    else:
        for i in range(10, 0, -1):
            if n >= i * factorial(i):
                return i + calc(n - i * factorial(i))
        return 0

if __name__ == '__main__':
    calc()