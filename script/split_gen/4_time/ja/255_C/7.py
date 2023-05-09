def solve(x, a, d, n):
    if d == 0:
        return 0 if x == a else -1
    if (x - a) % d != 0:
        return -1
    return max(0, (x - a) // d + 1)
