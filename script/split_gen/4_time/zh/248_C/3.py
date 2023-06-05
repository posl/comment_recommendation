def solve():
    N, M, K = map(int, input().split())
    dp = [[[0 for k in range(K+1)] for j in range(M+1)] for i in range(N+1)]
    dp[0][0][0] = 1
    for i in range(1, N+1):
        for j in range(1, M+1):
            for k in range(K+1):
                dp[i][j][k] += dp[i][j-1][k]
                if k >= j:
                    dp[i][j][k] += dp[i-1][j][k-j]
                dp[i][j][k] %= 998244353
    print(dp[N][M][K])
