def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # dp[i][j][k] = たこ焼きがj個、たい焼きがk個の時の最小個数
    dp = [[[float('inf')] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                if j + A[i] <= X and k + B[i] <= Y:
                    dp[i + 1][j + A[i]][k + B[i]] = min(dp[i + 1][j + A[i]][k + B[i]], dp[i][j][k] + 1)
    if dp[N][X][Y] == float('inf'):
        print(-1)
    else:
        print(dp[N][X][Y])
