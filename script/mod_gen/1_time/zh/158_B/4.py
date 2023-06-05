def f(n, a, b):
    if n == 0:
        return 0
    elif n == 1:
        return a
    elif n == 2:
        return a + b
    else:
        return f(n - 1, a, b) + f(n - 2, a, b)

if __name__ == '__main__':
    f()