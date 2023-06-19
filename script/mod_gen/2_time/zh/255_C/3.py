def solve(x,a,d,n):
    if d==0:
        if x==a:
            return 0
        else:
            return -1
    if n==1:
        if x==a:
            return 0
        else:
            return -1
    if (x-a)%d!=0:
        return -1
    else:
        return (x-a)//d
x,a,d,n=map(int,input().split())
print(solve(x,a,d,n))
