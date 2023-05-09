def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # dp[i][j] = i番目のお弁当までを使って、j個のたこ焼き、k個のたい焼きを作るのに必要な最小枚数
    dp = [[float("inf")] * (X + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                if j - A[i] >= 0 and k - B[i] >= 0:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - A[i]] + dp[i][k - B[i]] + 1)
                else:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
    if dp[N][X] == float("inf"):
        print(-1)
    else:
        print(dp[N][X])
