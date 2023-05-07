def f(x):
    if x < 10:
        return x
    else:
        return 9 + f(x // 10)

if __name__ == '__main__':
    f()