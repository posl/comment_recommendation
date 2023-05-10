def calc_height(n, m, x, t, d):
    height = t
    for i in range(m, x):
        height += d
    return height

if __name__ == '__main__':
    calc_height()