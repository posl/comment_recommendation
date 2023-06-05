def main():
    N, K = map(int, input().split())
    # N, K = 5, 3
    MOD = 10**9 + 7
    dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
    dp[0][0] = 1
    for i in range(1, K+1):
        for j in range(N+1):
            if j - i >= 0:
                dp[i][j] = (dp[i][j-i] + dp[i-1][j]) % MOD
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[K][N])
