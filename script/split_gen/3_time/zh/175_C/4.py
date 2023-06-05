def solve(x,k,d):
    x = abs(x)
    if x >= k*d:
        return x - k*d
    else:
        if (k*d-x)%2 == 0:
            return 0
        else:
            return min(abs(x-d),abs(x+d))
