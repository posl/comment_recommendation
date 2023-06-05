def solve(d,n):
    if d == 0:
        if n == 100:
            return 101
        else:
            return n
    elif d == 1:
        if n == 100:
            return 10100
        else:
            return 100*n
    else:
        if n == 100:
            return 1010000
        else:
            return 10000*n
