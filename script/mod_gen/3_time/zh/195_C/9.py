def f(n):
    s = str(n)
    if len(s) <= 3:
        return 0
    else:
        return int(s[:-3]) + 1

if __name__ == '__main__':
    f()