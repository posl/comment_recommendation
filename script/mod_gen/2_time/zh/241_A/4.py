def f(a):
    x = 0
    for i in range(10):
        x = a[x]
    return x

if __name__ == '__main__':
    f()