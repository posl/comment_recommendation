def solve(a,b,x):
    import math
    if a*a*b/2 >= x:
        return math.degrees(math.atan2(a*b*b,2*x))
    else:
        return math.degrees(math.atan2(2*(a*a*b-x),a*a*a))
