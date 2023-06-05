def solve(n):
    #dp[i][j]表示长度为i的数，首位为j的数的个数
    dp = [[0 for i in range(10)] for j in range(n+1)]
    for i in range(1,10):
        dp[1][i] = 1
    for i in range(2,n+1):
        for j in range(10):
            for k in range(10):
                if abs(j-k) <= 1:
                    dp[i][j] += dp[i-1][k]
                    dp[i][j] %= 998244353
    ans = 0
    for i in range(10):
        ans += dp[n][i]
        ans %= 998244353
    return ans

if __name__ == '__main__':
    solve()