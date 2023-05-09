def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = [0] * M
    Y = [0] * M
    for i in range(M):
        C[i], Y[i] = map(int, input().split())
    #dp[i][j]: i回目までのコイントスでj回連続表が出た時の最大金額
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        #i回目までのコイントスでj回連続表が出た時の最大金額
        for j in range(N + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            #表が出た時
            if X[i] == 1:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + X[i])
                for k in range(M):
                    if j + 1 == C[k]:
                        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + X[i] + Y[k])
            #裏が出た時
            else:
                dp[i + 1][0] = max(dp[i + 1][0], dp[i][j])
    ans = 0
    for i in range(N + 1):
        ans = max(ans, dp[N][i])
    print(ans)
