def f(x):
    if x < 10:
        return x
    else:
        return f(x // 10) + 1

if __name__ == '__main__':
    f()