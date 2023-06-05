def solve():
    n,k = map(int, input().split())
    mod = 10**9 + 7
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(k+1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % mod
            if i - j - 1 >= 0:
                dp[i][j] = (dp[i][j] - dp[i-j-1][j-1]) % mod
    print(dp[n][k])

if __name__ == '__main__':
    solve()