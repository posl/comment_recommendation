def main():
    N, K = map(int, input().split())
    mod = 10**9+7
    dp = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 1
    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % mod
    for i in range(1, K+1):
        ans = dp[N-K+1][i] * dp[K-1][i-1]
        print(ans%mod)
