def solve(n, x, a, b):
    for i in range(n):
        x -= a[i]
        if x < 0:
            return False
        x += b[i]
    return True
