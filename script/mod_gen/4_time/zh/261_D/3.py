def solve():
    N,M=map(int,input().split())
    X=list(map(int,input().split()))
    YC=[list(map(int,input().split())) for _ in range(M)]
    YC.sort(key=lambda x:x[0])
    YC.sort(key=lambda x:x[1],reverse=True)
    dp=[0]*(N+1)
    for i in range(N):
        dp[i+1]=max(dp[i+1],dp[i])
        for j in range(M):
            if i+YC[j][0]<=N:
                dp[i+YC[j][0]]=max(dp[i+YC[j][0]],dp[i]+X[i])
    print(max(dp))
solve()
