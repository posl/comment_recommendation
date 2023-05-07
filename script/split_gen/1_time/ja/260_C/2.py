def main():
    #入力
    N, X, Y = map(int, input().split())
    #初期化
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][1] = 1
    #漸化式
    for i in range(N):
        for j in range(N + 1):
            #赤い宝石を青い宝石に変換
            if j > 1:
                dp[i + 1][j - 1] += dp[i][j] * (j - 1)
            #青い宝石を赤い宝石に変換
            if j < N:
                dp[i + 1][j + 1] += dp[i][j] * (N - j)
            #青い宝石を赤い宝石に変換
            if j < N - 1:
                dp[i + 1][j + 2] += dp[i][j] * (N - j) * Y
            #赤い宝石を青い宝石に変換
            if j > 0:
                dp[i + 1][j] += dp[i][j] * j * X
    #出力
    print(dp[N][1])
