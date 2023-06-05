def solve():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    s=[0]*(n+1)
    for i in range(n):
        s[i+1]=s[i]+a[i]
    from collections import defaultdict
    d=defaultdict(int)
    for i in range(n+1):
        d[s[i]]+=1
    ans=0
    for i in range(n+1):
        ans+=d[s[i]-k]
        d[s[i]]-=1
    print(ans)
solve()
