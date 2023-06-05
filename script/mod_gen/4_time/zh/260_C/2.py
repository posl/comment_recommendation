def f(n, x, y):
    if n == 1:
        return 1
    elif n == 2:
        return x
    else:
        return f(n-1, x, y) + f(n-2, x, y) + y

if __name__ == '__main__':
    f()