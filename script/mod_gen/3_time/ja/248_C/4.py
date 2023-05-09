def main():
    N, M, K = map(int, input().split())
    mod = 998244353
    dp = [[0]*(M+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            dp[i][j] %= mod
    ans = 0
    for i in range(1, N+1):
        ans += dp[i-1][M] * dp[N-i][K-i*M] * M
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()