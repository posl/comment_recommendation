def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    MOD = 998244353
    # dp[i][j] = the number of ways to choose j terms from the first i terms
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N + 1):
            dp[i + 1][j] += dp[i][j] * 2
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j] %= MOD
            dp[i + 1][j + 1] %= MOD
    ans = 0
    for i in range(1, N + 1):
        ans += (dp[N][i] * A[i - 1]) % MOD
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()