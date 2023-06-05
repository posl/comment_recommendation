def solve(a, b, c):
    if a * c <= b:
        return c
    else:
        return b // a
