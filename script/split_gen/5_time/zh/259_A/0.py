def solve(n, m, x, t, d):
    height = t
    for i in range(1, n):
        if i >= x:
            height += d
        else:
            height += d
    return height
