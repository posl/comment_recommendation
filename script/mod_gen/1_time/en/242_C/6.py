def main():
    n = int(input())
    mod = 998244353
    dp = [[0] * 10 for _ in range(n)]
    dp[0] = [1] * 10
    for i in range(1, n):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i - 1][j + 1]
            elif j == 9:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
    print(sum(dp[n - 1]) % mod)

if __name__ == '__main__':
    main()