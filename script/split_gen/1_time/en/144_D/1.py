def solve(a, b, x):
    if x >= a * a * b / 2:
        return math.degrees(math.atan(2 * (a * a * b - x) / (a * a * a)))
    else:
        return math.degrees(math.atan(a * b * b / (2 * x)))
a, b, x = map(int, input().split())
print(solve(a, b, x))
