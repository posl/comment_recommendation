def main():
    N = int(input())
    mod = 998244353
    dp = [[0 for i in range(10)] for j in range(N + 1)]
    for i in range(1, 10):
        dp[1][i] = 1
    for i in range(2, N + 1):
        dp[i][0] = dp[i - 1][1]
        for j in range(1, 9):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % mod
        dp[i][9] = dp[i - 1][8]
    ans = 0
    for i in range(10):
        ans = (ans + dp[N][i]) % mod
    print(ans)

if __name__ == '__main__':
    main()