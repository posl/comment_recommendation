def solve():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    CY = [list(map(int,input().split())) for _ in range(M)]
    CY.sort(key=lambda x:x[1],reverse=True)
    dp = [[-1 for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(N):
            if dp[i][j] == -1:
                continue
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])
            for k in range(M):
                if j + CY[k][0] > N:
                    continue
                dp[i+CY[k][0]][j+CY[k][0]] = max(dp[i+CY[k][0]][j+CY[k][0]],dp[i][j]+CY[k][1])
    ans = 0
    for i in range(N+1):
        ans = max(ans,dp[N][i])
    print(ans)

if __name__ == '__main__':
    solve()