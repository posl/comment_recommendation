def main():
    N = int(input())
    mod = 998244353
    dp = [[0] * (N + 1) for _ in range(10)]
    for i in range(1, 10):
        dp[i][1] = 1
    for i in range(2, N + 1):
        for j in range(10):
            if j == 0:
                dp[j][i] = dp[1][i - 1]
            elif j == 9:
                dp[j][i] = dp[8][i - 1]
            else:
                dp[j][i] = (dp[j - 1][i - 1] + dp[j + 1][i - 1]) % mod
    print(sum(dp[i][N] for i in range(10)) % mod)

if __name__ == '__main__':
    main()