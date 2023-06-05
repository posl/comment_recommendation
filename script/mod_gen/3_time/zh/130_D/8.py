def solve():
    N,K=map(int,input().split())
    a=list(map(int,input().split()))
    s=[0]*(N+1)
    for i in range(N):
        s[i+1]=s[i]+a[i]
    ans=0
    right=0
    for left in range(N):
        while right<N and s[right+1]-s[left]<K:
            right+=1
        ans+=N-right
    print(ans)
solve()
