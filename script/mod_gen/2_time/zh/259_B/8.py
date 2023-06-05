def get_height(n, m, x, t, d):
    height = t
    if m <= x:
        for i in range(m, x):
            height += d
    else:
        for i in range(x, m):
            height -= d
    return height

if __name__ == '__main__':
    get_height()