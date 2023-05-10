def solve(x1, y1, x2, y2):
    if x1 == x2:
        return abs(y1-y2) == 2
    if y1 == y2:
        return abs(x1-x2) == 2
    return abs(x1-x2) == abs(y1-y2)
