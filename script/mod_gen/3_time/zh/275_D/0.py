def f(n):
    if n == 0:
        return 1
    return f(n // 2) + f(n // 3)

if __name__ == '__main__':
    f()