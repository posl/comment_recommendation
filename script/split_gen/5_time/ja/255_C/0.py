def solve(x,a,d,n):
    if d==0:
        if x==a:
            return 0
        else:
            return -1
    else:
        if (x-a)%d==0:
            k=(x-a)//d
            if k>=0 and k<=n-1:
                return k
            else:
                return -1
        else:
            return -1
