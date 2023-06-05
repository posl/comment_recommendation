def main():
    n = int(input())
    mod = 998244353
    dp = [[0 for i in range(10)] for j in range(n+1)]
    for i in range(1, 10):
        dp[1][i] = 1
    for i in range(2, n+1):
        for j in range(1, 10):
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % mod
        for j in range(1, 9):
            dp[i][j] = (dp[i][j] + dp[i-1][j+1]) % mod
    ans = 0
    for i in range(1, 10):
        ans = (ans + dp[n][i]) % mod
    print(ans)

if __name__ == '__main__':
    main()