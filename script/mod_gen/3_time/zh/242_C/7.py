def main():
    n = int(input())
    mod = 998244353
    dp = [[0] * 10 for i in range(n + 1)]
    dp[0] = [0] * 10
    dp[1] = [1] * 10
    for i in range(2, n + 1):
        dp[i][0] = dp[i - 1][1]
        dp[i][9] = dp[i - 1][8]
        for j in range(1, 9):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % mod
    ans = 0
    for i in range(10):
        ans = (ans + dp[n][i]) % mod
    print(ans)

if __name__ == '__main__':
    main()