def main():
    N = int(input())
    mod = 998244353
    dp = [[0]*(N+1) for _ in range(10)]
    for i in range(1,10):
        dp[i][1] = 1
    for j in range(2,N+1):
        for i in range(10):
            if i == 0:
                dp[i][j] = dp[i+1][j-1]
            elif i == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i+1][j-1]
            dp[i][j] = dp[i][j] % mod
    print(sum(dp[i][N] for i in range(1,10)) % mod)

if __name__ == '__main__':
    main()