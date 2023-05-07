def main():
    N = int(input())
    MOD = 998244353
    dp = [[0] * 10 for _ in range(N)]
    dp[0] = [1] * 10
    for i in range(1, N):
        dp[i][0] = dp[i - 1][1]
        dp[i][9] = dp[i - 1][8]
        for j in range(1, 9):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
        dp[i] = [x % MOD for x in dp[i]]
    print(sum(dp[N - 1]) % MOD)

if __name__ == '__main__':
    main()