def solve():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    # dp[i][j] = i回目のコイントスで、カウンタの数値がjであるときの、最大のもらえる金額
    dp = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        dp[i][0] = dp[i-1][N]
        for j in range(1, N+1):
            dp[i][j] = max(dp[i-1][j-1] + X[i-1], dp[i-1][N])
            for k in range(M):
                if j == C[k]:
                    dp[i][j] = max(dp[i][j], dp[i-1][0] + Y[k])
    ans = 0
    for i in range(N+1):
        ans = max(ans, dp[N][i])
    print(ans)

if __name__ == '__main__':
    solve()