def solve(a, b, x):
    if a * a * b / 2 > x:
        return math.atan(a * b * b / (2 * x))
    else:
        return math.atan(2 * (a * a * b - x) / (a * a * a))
import math
a, b, x = map(int, input().split())
print(math.degrees(solve(a, b, x)))
