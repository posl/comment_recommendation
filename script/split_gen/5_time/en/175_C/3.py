def solve(x, k, d):
    x = abs(x)
    if x > k * d:
        return x - k * d
    else:
        k -= x // d
        x %= d
        if k % 2 == 0:
            return x
        else:
            return d - x
