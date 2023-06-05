def get_height(n, m, x, t, d):
    height = t
    for i in range(1, n):
        if i == x:
            continue
        height += d
    return height
