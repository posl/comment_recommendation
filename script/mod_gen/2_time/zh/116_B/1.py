def calc(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int(3 * n + 1)

if __name__ == '__main__':
    calc()