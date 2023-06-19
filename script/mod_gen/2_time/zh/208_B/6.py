def f(n):
    return 1 if n <= 1 else n * f(n-1)

if __name__ == '__main__':
    f()