def solve(a, b, x):
    if x <= a*a*b/2:
        return 90 - 2 * math.degrees(math.atan(2*x/(a*b*b)))
    else:
        return math.degrees(math.atan(2*(a*a*b-x)/(a*a*a)))
