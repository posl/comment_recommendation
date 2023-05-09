def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    # A[i][j] = A[j][i]
    for i in range(N):
        for j in range(i):
            A[i][j] = A[j][i]
    # dp[i][j]: i番目までの人がj番目までの2人組を選んだときの最大値
    # dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] ^ A[i-1][j-1])
    dp = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] ^ A[i-1][j-1])
    print(dp[N][N])

if __name__ == '__main__':
    main()