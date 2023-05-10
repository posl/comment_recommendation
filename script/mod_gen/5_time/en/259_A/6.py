def get_height(n, m, x, t, d):
    height = t
    for i in range(x, n):
        height += d
    for i in range(m, x):
        height += d
    return height

if __name__ == '__main__':
    get_height()