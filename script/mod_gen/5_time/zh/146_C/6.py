def d(n):
    if n < 10:
        return 1
    else:
        return 1 + d(n // 10)

if __name__ == '__main__':
    d()