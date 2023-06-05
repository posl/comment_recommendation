def solve(a,b,x):
    import math
    if a*a*b/2.0 > x:
        return math.atan(a*b*b/2.0/x)/math.pi*180
    else:
        return math.atan(2*(b-x/(a*a))/a)/math.pi*180

if __name__ == '__main__':
    solve()