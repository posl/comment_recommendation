def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[[0] * (X + 1) for _ in range(Y + 1)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(Y + 1):
            for k in range(X + 1):
                if j >= B[i] and k >= A[i]:
                    dp[i + 1][j][k] = max(dp[i][j][k], dp[i][j - B[i]][k - A[i]] + 1)
                else:
                    dp[i + 1][j][k] = dp[i][j][k]
    if dp[N][Y][X] == 0:
        print(-1)
    else:
        print(N - dp[N][Y][X])
