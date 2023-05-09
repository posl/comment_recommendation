def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[[0] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                if j >= A[i] and k >= B[i]:
                    dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j - A[i]][k - B[i]] + 1)
                dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
    ans = dp[N][X][Y]
    if ans == 0:
        ans = -1
    print(ans)
