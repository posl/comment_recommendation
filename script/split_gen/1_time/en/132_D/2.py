def main():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * (K+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        dp[i][0] = 1
        for j in range(1, K+1):
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % MOD
    for i in range(1, K+1):
        print((dp[N-K][i] * dp[K-1][i-1]) % MOD)
