def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    C = []
    Y = []
    for i in range(M):
        c, y = map(int, input().split())
        C.append(c)
        Y.append(y)
    # dp[i][j] : i回目のコイントスまでで、カウンタがjになっているときの最大金額
    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(N + 1):
            # 表が出たとき
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + X[i])
            # 裏が出たとき
            if j > 0:
                dp[i + 1][j - 1] = max(dp[i + 1][j - 1], dp[i][j])
        for k in range(M):
            if C[k] == i + 1:
                for j in range(N):
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j] + Y[k])
    print(max(dp[N]))
