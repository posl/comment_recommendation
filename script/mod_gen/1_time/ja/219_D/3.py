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
                    dp[i + 1][j][k] = max(dp[i][j][k], dp[i][j - A[i]][k - B[i]] + 1)
                else:
                    dp[i + 1][j][k] = dp[i][j][k]
    if dp[N][X][Y] > 0:
        print(N - dp[N][X][Y])
    else:
        print(-1)

if __name__ == '__main__':
    main()