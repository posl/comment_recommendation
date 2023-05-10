def solve():
    #n,k=map(int,input().split())
    #a=list(map(int,input().split()))
    n,k=3,7
    a=[1,6,3]
    b=bin(k)
    c=len(b)-2
    d=[0]*c
    for i in range(c):
        for j in range(n):
            d[i]+=((a[j]>>i)&1)
    ans=0
    for i in range(c-1,-1,-1):
        if d[i]<n/2:
            if ans+(1<<i)<=k:
                ans+=(1<<i)
    e=0
    for i in range(n):
        e+=ans^a[i]
    print(e)
    return 0

if __name__ == '__main__':
    solve()