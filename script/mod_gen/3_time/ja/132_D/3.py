def main():
    N, K = map(int, input().split())
    mod = 10**9+7
    # dp[i][j] := i 個のボールを j 個のグループに分けるときの分け方の数
    dp = [[0] * (N+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(1, N+1):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j] * j) % mod
    for i in range(1, K+1):
        print(dp[N-K+1][i] * dp[K-1][i-1] % mod)

if __name__ == '__main__':
    main()