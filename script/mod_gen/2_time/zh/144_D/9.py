def get_angle(a, b, x):
    if x > a * a * b / 2:
        return 90 - get_angle(a, b, a * a * b - x)
    return math.degrees(math.atan(2 * x / a / b / b))
import math
a, b, x = map(int, input().split())
print(get_angle(a, b, x))
