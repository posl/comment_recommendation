def solve(n, ab):
    s = 0
    for a, b in ab:
        s += a / b
    t = s / 2
    s = 0
    for a, b in ab:
        if a / b < t:
            s += a
        else:
            s += t * b
            break
    return s
