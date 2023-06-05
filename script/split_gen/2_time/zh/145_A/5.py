def solve(a, b, x):
    import math
    if x >= a*a*b/2:
        ans = math.degrees(math.atan(2*(a*a*b-x)/(a*a*a)))
    else:
        ans = math.degrees(math.atan((a*b*b)/(2*x)))
    return ans
