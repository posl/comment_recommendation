def solve():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    s=[0]*(n+1)
    for i in range(n):
        s[i+1]=s[i]+a[i]
    ans=0
    r=0
    for l in range(n):
        while r<n and s[r+1]-s[l]<k:
            r+=1
        ans+=n-r
    print(ans)
