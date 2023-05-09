def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    for i in range(M):
        A[i], B[i], C[i] = map(int, input().split())
    INF = 10**18
    dp = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][i] = 0
    for i in range(M):
        dp[A[i]][B[i]] = C[i]
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if dp[i][j] == dp[i][k] + dp[k][j]:
                    ans += dp[i][j]
    print(ans)
