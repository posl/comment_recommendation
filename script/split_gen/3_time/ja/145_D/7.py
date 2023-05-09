def main():
    n, m = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n + 1):
        for j in range(m + 1):
            if i + 1 <= n and j + 2 <= m:
                dp[i + 1][j + 2] += dp[i][j]
                dp[i + 1][j + 2] %= MOD
            if i + 2 <= n and j + 1 <= m:
                dp[i + 2][j + 1] += dp[i][j]
                dp[i + 2][j + 1] %= MOD
    print(dp[n][m])
