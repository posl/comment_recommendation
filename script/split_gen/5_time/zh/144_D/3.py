def solve(a, b, x):
    import math
    if x > a*a*b/2:
        return math.atan(2*(a*a*b-x)/(a*a*a))
    else:
        return math.atan((a*b*b)/(2*x))
