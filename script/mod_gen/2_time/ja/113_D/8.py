def main():
    # H:高さ, W:幅, K:最終的にたどり着く縦棒の番号
    H, W, K = map(int, input().split())
    # dp[i][j]:i段目のj番目の縦棒の上端から下にたどり着くあみだくじの本数
    dp = [[0 for _ in range(W)] for _ in range(H + 1)]
    # i段目のj番目の縦棒の上端から下にたどり着くあみだくじの本数を計算する
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if j == 0:
                dp[i + 1][j] = dp[i][j] + dp[i][j + 1]
                dp[i + 1][j] %= 1000000007
            elif j == W - 1:
                dp[i + 1][j] = dp[i][j] + dp[i][j - 1]
                dp[i + 1][j] %= 1000000007
            else:
                dp[i + 1][j] = dp[i][j - 1] + dp[i][j] + dp[i][j + 1]
                dp[i + 1][j] %= 1000000007
    # 答えを出力する
    print(dp[H][K - 1])

if __name__ == '__main__':
    main()