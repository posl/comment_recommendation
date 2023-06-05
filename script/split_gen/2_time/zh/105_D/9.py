def solve(n,m,a):
    c=[0]
    for i in range(n):
        c.append(c[-1]+a[i])
    d={}
    for i in range(n+1):
        c[i]%=m
        if c[i] in d:
            d[c[i]]+=1
        else:
            d[c[i]]=1
    ans=0
    for i in d:
        ans+=d[i]*(d[i]-1)//2
    return ans
n,m=map(int,input().split())
a=list(map(int,input().split()))
print(solve(n,m,a))
