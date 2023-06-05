def f(m, A):
    res = 0
    for a in A:
        res += m % a
    return res

if __name__ == '__main__':
    f()