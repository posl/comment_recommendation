def get_height(n, m, x, t, d):
    height = t
    for i in range(1, x):
        height += d
    for i in range(x, m):
        height += d
    for i in range(m, n):
        height += d
    return height
