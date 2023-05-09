def calc(n, x, y):
    if n == 1:
        return 1
    elif n == 2:
        return x + y
    else:
        return calc(n-1, x, y) + calc(n-2, x, y)

if __name__ == '__main__':
    calc()