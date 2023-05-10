def solve():
    H, W, K = map(int, input().split())
    MOD = 10**9+7
    dp = [[0 for _ in range(W)] for _ in range(H+1)]
    dp[0][0] = 1
    for i in range(1, H+1):
        for j in range(W):
            if j == 0:
                dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
            elif j == W-1:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
            dp[i][j] %= MOD
    print(dp[H][K-1])
