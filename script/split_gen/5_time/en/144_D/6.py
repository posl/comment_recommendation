def solve(a, b, x):
    if a*a*b/2 >= x:
        return 90 - 2*x/(a*b*b)*180
    else:
        return 2*(a*a*b-x)/(a*a*a)*180
