def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    dp = [[[0] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
                if j - A[i] >= 0 and k - B[i] >= 0:
                    dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j - A[i]][k - B[i]] + 1)
    if dp[N][X][Y] == 0:
        print(-1)
    else:
        print(dp[N][X][Y])
