def solve(a, b, x):
    import math
    if x <= a * a * b / 2:
        ans = math.atan(a * b * b / 2 / x) * 180 / math.pi
    else:
        ans = math.atan(2 * (b - x / a / a) / a) * 180 / math.pi
    return ans
