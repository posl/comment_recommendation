def f(n):
    if n == 0:
        return 0
    else:
        g1 = int("".join(sorted(str(n), reverse=True)))
        g2 = int("".join(sorted(str(n), reverse=False)))
        return g1 - g2

if __name__ == '__main__':
    f()