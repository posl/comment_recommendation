def solve():
    N, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * (K+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(K+1):
            if j < K:
                dp[i+1][j+1] = (dp[i+1][j+1] + dp[i][j]) % MOD
            dp[i+1][j] = (dp[i+1][j] + dp[i][j] * (N - i - j)) % MOD
    print(dp[N][K])
