def main():
    H, W, K = map(int, input().split())
    #print(H, W, K)
    # dp[縦棒の数][横線の数]
    dp = [[0 for i in range(W+1)] for j in range(H+1)]
    # 初期値
    dp[0][0] = 1
    # dp[縦棒の数][横線の数] = dp[縦棒の数-1][横線の数-1] + dp[縦棒の数-1][横線の数] + dp[縦棒の数-1][横線の数+1]
    for i in range(1, H+1):
        for j in range(W+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
            elif j == W:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
    #print(dp)
    print(dp[H][K-1] % 1000000007)
