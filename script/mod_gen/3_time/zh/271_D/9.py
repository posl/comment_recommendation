def f(n, s, a, b):
    if n == 0:
        return s == 0
    if f(n-1, s-a[n-1], a, b):
        print('T', end='')
        return True
    if f(n-1, s-b[n-1], a, b):
        print('H', end='')
        return True
    return False

if __name__ == '__main__':
    f()