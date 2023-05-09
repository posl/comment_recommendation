def solve():
    n=int(input())
    a=list(map(int,input().split()))
    ans=2**30
    for i in range(2**(n-1)):
        now=0
        tmp=0
        for j in range(n):
            tmp|=a[j]
            if (i>>j)&1:
                now^=tmp
                tmp=0
        now^=tmp
        ans=min(ans,now)
    print(ans)
