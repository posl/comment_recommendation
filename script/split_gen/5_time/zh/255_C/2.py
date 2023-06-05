def solve(x,a,d,n):
    if d==0:
        if x==a:
            return 0
        else:
            return 1
    if n==1:
        if x==a:
            return 0
        else:
            return 1
    if n==2:
        if x==a:
            return 0
        else:
            return 2
    if d>0:
        if x<a:
            return 1
        else:
            if (x-a)%d==0:
                return (x-a)//d
            else:
                return (x-a)//d+1
    if d<0:
        if x>a:
            return 1
        else:
            if (a-x)%d==0:
                return (a-x)//d
            else:
                return (a-x)//d+1
