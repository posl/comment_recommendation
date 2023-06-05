def d(n):
    if n == 0:
        return 0
    else:
        return n % 10 + d(n // 10)

if __name__ == '__main__':
    d()