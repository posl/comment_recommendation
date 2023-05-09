def main():
    H, W, A, B = map(int, input().split())
    N = H * W
    # 初期化
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N):
            if i + 1 <= N:
                dp[i + 1][j] += dp[i][j]
            if j + 1 <= N:
                dp[i][j + 1] += dp[i][j]
    # dp[i][j]: i個の2*1のタイルとj個の1*1のタイルを使ってN個のマスを埋め尽くす方法の数
    # dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # dp[i][j]: i個の2*1のタイルとj個の1*1のタイルを使ってN個のマスを埋め尽くす方法の数
    # dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # 1*1のタイルを使わない場合
    # dp[i][0] = dp[i-1][0]
    # 2*1のタイルを使わない場合
    # dp[0][j] = dp[0][j-1]
    # dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # 1*1のタイルを使わない場合
    # dp[i][0] = dp[i-1][0]
    # 2*1のタイルを使わない場合
    # dp[0][j] = dp[0][j-1]
    # N個のマスを埋め尽くす方法の数
    ans = 0
    for i in range(A + 1):
        j = N - 2
