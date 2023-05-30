def solve(a, b, x):
    if x * 2 < a * a * b:
        return math.atan(a * b * b / (2 * x)) * 180 / math.pi
    else:
        return math.atan(2 * (a * a * b - x) / (a * a * a)) * 180 / math.pi
import math
a, b, x = map(int, input().split())
print(solve(a, b, x))
