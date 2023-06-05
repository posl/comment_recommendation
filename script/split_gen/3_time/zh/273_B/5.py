def solve(x,k):
    if x==0:
        return 0
    res=x
    for i in range(1,k+1):
        tmp=round(x/(10**i))*(10**i)
        res=min(res,abs(x-tmp))
    return res
