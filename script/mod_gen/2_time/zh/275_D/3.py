def f(x):
    if x == 0:
        return 1
    return f(x//2) + f(x//3)

if __name__ == '__main__':
    f()