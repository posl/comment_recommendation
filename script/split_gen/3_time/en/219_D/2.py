def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [[[float('inf')] * (X + 1) for _ in range(Y + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i in range(1, N + 1):
        for j in range(Y + 1):
            for k in range(X + 1):
                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k])
                if j - B[i - 1] >= 0 and k - A[i - 1] >= 0:
                    dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j - B[i - 1]][k - A[i - 1]] + 1)
    ans = min(dp[N][Y][X], dp[N][Y - 1][X], dp[N][Y][X - 1])
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
