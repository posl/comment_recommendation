def d(n):
    if n < 10:
        return 1
    else:
        return d(n // 10) + 1

if __name__ == '__main__':
    d()