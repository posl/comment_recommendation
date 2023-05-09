def main():
    N, W = map(int, input().split())
    A = [None] * N
    B = [None] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # dp[i][j] = (i番目までのチーズを使って, 重さjのときの価値の最大値)
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(W + 1):
            if j - A[i] >= 0:
                dp[i + 1][j] = max(dp[i][j], dp[i + 1][j - A[i]] + B[i])
            else:
                dp[i + 1][j] = dp[i][j]
    print(dp[N][W])

if __name__ == '__main__':
    main()