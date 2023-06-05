def solve(a, b, x):
    import math
    if x <= (a ** 2 * b) / 2:
        return math.degrees(math.atan((a * b ** 2) / (2 * x)))
    else:
        return math.degrees(math.atan(2 * (a ** 2 * b - x) / (a ** 3)))

if __name__ == '__main__':
    solve()