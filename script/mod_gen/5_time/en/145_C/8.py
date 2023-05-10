def f(x):
    if x <= 1:
        return 1
    return x * f(x-1)

if __name__ == '__main__':
    f()