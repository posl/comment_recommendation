def solve(x, a, d, n):
    if d == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    if d > 0:
        x = x - a
    else:
        x = a - x
    if x % d == 0:
        return int(abs(x / d))
    else:
        return int(abs(x / d) + 1)
