def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    CY = [list(map(int, input().split())) for _ in range(M)]
    #dp[n][m]表示第n次投掷后，连续投掷m次的最大金额
    dp = [[0]*(M+1) for _ in range(N+1)]
    for n in range(1, N+1):
        for m in range(1, M+1):
            c, y = CY[m-1]
            if n < c: dp[n][m] = dp[n][m-1]
            else:
                dp[n][m] = max(dp[n][m-1], dp[n-c][m-1] + y)
    #print(dp)
    ans = 0
    for n in range(N+1):
        ans = max(ans, dp[n][M] + sum(X[:n]))
    print(ans)
