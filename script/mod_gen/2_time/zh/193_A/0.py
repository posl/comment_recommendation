def f(x, n):
    if x == 0:
        return 0
    else:
        return f(x//n, n) + x%n

if __name__ == '__main__':
    f()