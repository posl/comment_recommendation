def main():
    H, W, K = map(int, input().split())
    MOD = 1000000007
    # dp[i][j] : i段目でj番目の縦線にいるあみだくじの本数
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    dp[0][1] = 1
    for i in range(H):
        for j in range(1, W + 1):
            # 左に移動
            if j > 1:
                dp[i + 1][j - 1] += dp[i][j]
                dp[i + 1][j - 1] %= MOD
            # 右に移動
            if j < W:
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j + 1] %= MOD
            # 移動しない
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD
    print(dp[H][K])
