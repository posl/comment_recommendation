def solve(x, k, d):
    if x < 0:
        x = -x
    if x // d >= k:
        return x - k * d
    elif (k - x // d) % 2 == 0:
        return x - (x // d) * d
    else:
        return d - x + (x // d) * d
