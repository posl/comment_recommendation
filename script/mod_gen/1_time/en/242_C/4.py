def main():
    n = int(input())
    mod = 998244353
    dp = [[0] * 10 for _ in range(2)]
    for i in range(1, 10):
        dp[0][i] = 1
    for i in range(n - 1):
        for j in range(10):
            dp[(i + 1) % 2][j] = 0
        for j in range(10):
            if j == 0:
                dp[(i + 1) % 2][j + 1] += dp[i % 2][j]
                dp[(i + 1) % 2][j + 1] %= mod
            elif j == 9:
                dp[(i + 1) % 2][j - 1] += dp[i % 2][j]
                dp[(i + 1) % 2][j - 1] %= mod
            else:
                dp[(i + 1) % 2][j - 1] += dp[i % 2][j]
                dp[(i + 1) % 2][j + 1] += dp[i % 2][j]
                dp[(i + 1) % 2][j - 1] %= mod
                dp[(i + 1) % 2][j + 1] %= mod
    print(sum(dp[(n - 1) % 2]) % mod)

if __name__ == '__main__':
    main()