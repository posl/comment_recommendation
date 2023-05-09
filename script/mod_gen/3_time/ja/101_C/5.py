def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    # dp[i][j]: i番目までの要素で、j回操作したときの最小値
    dp = [[float('inf')] * (N+1) for _ in range(N+1)]
    # 初期化
    for i in range(1, N+1):
        dp[i][0] = A[i]
    # DP
    for i in range(1, N+1):
        for j in range(1, N+1):
            # 操作回数が要素数を超える場合は、前回の操作回数を継承
            if i - K < 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j])
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-K][j-1])
    print(dp[N][N])

if __name__ == '__main__':
    main()