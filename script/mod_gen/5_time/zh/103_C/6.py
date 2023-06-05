def f(m, a):
    s = 0
    for i in range(len(a)):
        s += m % a[i]
    return s

if __name__ == '__main__':
    f()