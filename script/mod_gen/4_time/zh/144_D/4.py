def solve(a, b, x):
    if a*a*b/2.0 >= x:
        return math.atan(a*b*b/2.0/x)/math.pi*180.0
    else:
        return math.atan(2.0*(a*a*b-x)/(a*a*a))/math.pi*180.0

if __name__ == '__main__':
    solve()