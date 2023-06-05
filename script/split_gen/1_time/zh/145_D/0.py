def solve(x,y):
    if (x+y)%3 != 0:
        return 0
    else:
        n = int((2*y-x)/3)
        m = int((2*x-y)/3)
        if n<0 or m<0:
            return 0
        else:
            return comb(n+m,n,10**9+7)
