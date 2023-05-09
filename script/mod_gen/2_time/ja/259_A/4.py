def calc_height(n, m, x, t, d):
    height = t
    for i in range(1, m):
        height += d
    for i in range(m, n):
        height += d
        if i == x:
            continue
    return height

if __name__ == '__main__':
    calc_height()