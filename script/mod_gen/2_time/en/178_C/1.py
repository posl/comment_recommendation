def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [[0]*10 for _ in range(N+1)]
    for i in range(1, 10):
        dp[1][i] = 1
    for i in range(2, N+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    print(sum(dp[N])%MOD)

if __name__ == '__main__':
    main()