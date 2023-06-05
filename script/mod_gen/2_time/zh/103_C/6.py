def f(m, a):
    res = 0
    for i in a:
        res += m % i
    return res

if __name__ == '__main__':
    f()