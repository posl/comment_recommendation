def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[[float("inf")] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(X + 1):
            for k in range(Y + 1):
                if j >= A[i] and k >= B[i]:
                    dp[i + 1][j][k] = min(dp[i][j][k], dp[i][j - A[i]][k - B[i]] + 1)
                else:
                    dp[i + 1][j][k] = min(dp[i][j][k], dp[i][j][k])
    ans = dp[N][X][Y]
    if ans == float("inf"):
        ans = -1
    print(ans)
