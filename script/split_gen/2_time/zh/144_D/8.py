def solve(a, b, x):
    if x > a*a*b/2:
        return 90 - solve(a, b, a*a*b-x)
    else:
        return 90 - math.degrees(math.atan(2*x/(a*b*b)))
import math
a, b, x = map(int, input().split())
print(solve(a, b, x))
