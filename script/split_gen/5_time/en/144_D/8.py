def find_angle(a, b, x):
    if x > a**2*b/2:
        return 90 - math.atan(2*(a**2*b-x)/(a**3))
    else:
        return math.atan(a*b**2/(2*x))
