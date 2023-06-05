def solve():
    n,l,r=map(int,input().split())
    a=list(map(int,input().split()))
    ans=sum(a)
    for i in range(1,n):
        a[i]=min(a[i-1]*2,l+r)
    for i in range(n-1,-1,-1):
        if i<n-1:
            a[i]=min(a[i],a[i+1]*2)
        ans+=a[i]
    print(ans)
solve()
