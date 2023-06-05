def height(n, m, x, t, d):
    if n < m or n < x or x < 1 or m < 0 or n < 0 or t < 1 or d < 1:
        return -1
    if n == m:
        return t
    if x == 1:
        return t + (n - m) * d
    return height(n, m, x - 1, t, d) + d
