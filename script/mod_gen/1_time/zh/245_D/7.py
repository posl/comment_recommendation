def f(x):
    return sum([a[i] * x ** i for i in range(n + 1)])

if __name__ == '__main__':
    f()