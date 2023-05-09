def solve():
    N = int(input())
    dp = [[0]*10 for _ in range(N)]
    MOD = 998244353
    for i in range(1, 10):
        dp[0][i] = 1
    for i in range(1, N):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
            dp[i][j] %= MOD
    print(sum(dp[-1]) % MOD)

if __name__ == '__main__':
    solve()