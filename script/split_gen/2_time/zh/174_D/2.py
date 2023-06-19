def solve(n, c):
    w = c.count('W')
    r = c.count('R')
    if w == 0 or r == 0:
        return 0
    if w == r:
        return 1
    if w > r:
        return r
    if w < r:
        return w
