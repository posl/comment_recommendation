def calc(n, x, y):
    if n == 1:
        return 0
    if n == 2:
        return x
    # 1级红宝石
    r1 = 1
    # 2级红宝石
    r2 = 0
    # 1级蓝宝石
    b1 = 0
    # 2级蓝宝石
    b2 = 0
    for i in range(2, n + 1):
        b2 = b1
        b1 = r2 * y
        r2 = r1
        r1 = b2 + x
    return b1

if __name__ == '__main__':
    calc()