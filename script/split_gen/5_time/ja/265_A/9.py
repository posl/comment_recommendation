def solve(x, y, n):
    if n % 3 == 0:
        return n // 3 * y
    else:
        return (n // 3 + 1) * y - x
