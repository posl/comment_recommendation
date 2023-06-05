def f(x, m):
    d = int(max(x))
    n = d+1
    while True:
        if int(x, n) <= m:
            n += 1
        else:
            break
    return n - d - 1

if __name__ == '__main__':
    f()