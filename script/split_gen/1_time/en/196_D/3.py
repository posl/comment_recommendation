def solve(h, w, a, b):
    if h == 1:
        return 1
    if w == 1:
        return 1
    if a == 0:
        return 1
    if b == 0:
        return 1
    return solve(h - 1, w, a - 1, b) + solve(h, w - 1, a, b - 1)
