def f(x):
    r = 0
    for i in range(1, x + 1):
        if x % i == 0:
            r += 1
    return r

if __name__ == '__main__':
    f()