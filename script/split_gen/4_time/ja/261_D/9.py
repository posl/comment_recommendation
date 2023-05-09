def solve():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    XY = [list(map(int,input().split())) for _ in range(M)]
    dp = [[-1]*(N+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(N):
            if dp[i][j] == -1:
                continue
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+X[i])
            for k in range(M):
                if j+1 == XY[k][0]:
                    dp[i+1][0] = max(dp[i+1][0],dp[i][j]+XY[k][1])
    ans = 0
    for i in range(N+1):
        ans = max(ans,dp[N][i])
    print(ans)
