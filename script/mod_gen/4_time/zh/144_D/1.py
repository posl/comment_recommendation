def solve(a,b,x):
    import math
    if x >= a*a*b/2:
        return math.atan(2*(a*a*b-x)/(a*a*a))*180/math.pi
    else:
        return math.atan(a*b*b/(2*x))*180/math.pi

if __name__ == '__main__':
    solve()