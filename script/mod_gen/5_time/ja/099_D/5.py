def calc_min_cost(N, C, D, c):
    # dp[i][j] := i 行目まで塗り終わった時の、i 行目の色が j の場合の最小コスト
    dp = [[float('inf')] * C for _ in range(N)]
    for j in range(C):
        dp[0][j] = D[c[0]][j]
    for i in range(1, N):
        for j in range(C):
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + D[c[i - 1]][j])
        for j in range(C):
            for k in range(C):
                dp[i][j] = min(dp[i][j], dp[i - 1][k] + D[c[i - 1]][j])
    return min(dp[-1])

if __name__ == '__main__':
    calc_min_cost()