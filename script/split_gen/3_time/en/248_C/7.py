def solve():
    N, M, K = map(int, input().split())
    mod = 998244353
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(K + 1):
            for k in range(M + 1):
                if j + k <= K:
                    dp[i + 1][j + k] += dp[i][j]
                    dp[i + 1][j + k] %= mod
    print(dp[N][K])
