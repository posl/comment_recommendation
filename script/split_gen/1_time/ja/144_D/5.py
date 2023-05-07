def solve(a, b, x):
    if x <= a * a * b / 2:
        return math.degrees(math.atan(2 * x / (a * a * b)))
    else:
        return math.degrees(math.atan(2 * (a * a * b - x) / (a * a * a)))
