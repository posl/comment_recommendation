def count2(n):
    c = 0
    while n % 2 == 0:
        n = n / 2
        c += 1
    return c

if __name__ == '__main__':
    count2()