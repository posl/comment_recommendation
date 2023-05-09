def main():
    H, W, K = map(int, input().split())
    MOD = 10**9 + 7
    dp = [[0] * W for _ in range(H+1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if j == 0:
                dp[i+1][j] = dp[i][j+1]
            elif j == W-1:
                dp[i+1][j] = dp[i][j-1]
            else:
                dp[i+1][j] = dp[i][j-1] + dp[i][j+1]
    print(dp[H][K-1]%MOD)
