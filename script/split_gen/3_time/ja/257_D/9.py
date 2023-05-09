def main():
    N = int(input())
    XYP = [tuple(map(int, input().split())) for _ in range(N)]
    INF = 10 ** 18
    # dp[i][j] = i番目までのジャンプ台で、j回訓練したときの最小のジャンプ力
    dp = [[INF] * (N + 1) for _ in range(N)]
    for i in range(N):
        dp[i][0] = 0
    for i in range(N):
        for j in range(1, N):
            # i番目のジャンプ台を使わない
            dp[i][j] = min(dp[i][j], dp[i][j - 1])
            # i番目のジャンプ台を使う
            for k in range(N):
                if i == k:
                    continue
                if XYP[i][2] * j >= abs(XYP[i][0] - XYP[k][0]) + abs(XYP[i][1] - XYP[k][1]):
                    dp[k][j] = min(dp[k][j], j)
    ans = INF
    for i in range(N):
        ans = min(ans, max(dp[i]))
    print(ans)
