def f(n):
    s = 0
    while n > 0:
        s += 1
        n //= 10
    return s

if __name__ == '__main__':
    f()