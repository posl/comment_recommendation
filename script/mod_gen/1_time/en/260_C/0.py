def calc(n, x, y):
    if n == 1:
        return 0
    elif n == 2:
        return x
    else:
        return calc(n-1, x, y) + x + (n-2)*y

if __name__ == '__main__':
    calc()