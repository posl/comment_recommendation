def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # dp[i][j] = i番目のステージをj回クリアするのにかかる最小時間
    dp = [[float("inf")] * (X + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(X + 1):
            # i番目のステージをj回クリアするのにかかる最小時間
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + AB[i][0] + AB[i][1] * j)
            # i番目のステージをj回クリアするのにかかる最小時間
            if j > 0:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i + 1][j - 1] + AB[i][1])
    print(dp[-1][-1])
