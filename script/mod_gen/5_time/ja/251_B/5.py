def main():
    N, W = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(W + 1):
            dp[i + 1][j] = dp[i][j]
            if j >= A[i]:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - A[i]] + A[i])
    print(dp[N][W])

if __name__ == '__main__':
    main()