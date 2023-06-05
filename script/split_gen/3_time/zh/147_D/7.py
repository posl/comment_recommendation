def solve():
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(60):
        x=0
        for j in range(n):
            if a[j]>>i&1:
                x+=1
        ans+=x*(n-x)*(1<<i)
        ans%=1000000007
    print(ans)
