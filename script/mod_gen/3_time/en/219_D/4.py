def main():
    N = int(input())
    X, Y = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # dp[i][j] = i種類の食べ物をj個買うときの最小個数
    # dp[i][j] = min(dp[i-1][j], dp[i-1][j-A[i]] + 1) if j >= A[i]
    # dp[i][j] = dp[i-1][j] if j < A[i]
    # dp[i][j] = min(dp[i][j], dp[i-1][j-B[i]] + 1) if j >= B[i]
    # dp[i][j] = dp[i][j] if j < B[i]
    dp = [[float('inf')] * (X + Y + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(1, N + 1):
        for j in range(X + Y + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= A[i - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - A[i - 1]] + 1)
            if j >= B[i - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - B[i - 1]] + 1)
    ans = float('inf')
    for i in range(X, X + Y + 1):
        ans = min(ans, dp[N][i])
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

if __name__ == '__main__':
    main()