def solve(a, b, x):
    if x >= a * a * b / 2:
        return 90 - solve(a, b, a * a * b - x)
    return math.atan2(2 * x, a * b * b) * 180 / math.pi
