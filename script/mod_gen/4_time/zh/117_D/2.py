def f(x, a):
    s = 0
    for i in range(len(a)):
        s += x ^ a[i]
    return s

if __name__ == '__main__':
    f()