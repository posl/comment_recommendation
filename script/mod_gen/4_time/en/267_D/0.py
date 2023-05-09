def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(M):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + (i + 1) * A[i])
            if i + 2 <= N:
                dp[i + 2][j + 1] = max(dp[i + 2][j + 1], dp[i][j] + (i + 1) * A[i + 1])
    print(dp[N][M])

if __name__ == '__main__':
    main()