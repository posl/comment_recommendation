def solve(x,a,d,n):
    if d == 0:
        if x == a:
            return 0
        else:
            return 1
    else:
        if (x - a) % d == 0 and (x - a) // d >= 0:
            return (x - a) // d
        else:
            return 1
