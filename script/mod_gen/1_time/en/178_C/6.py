def main():
    import sys
    N = int(sys.stdin.readline())
    MOD = 10**9 + 7
    dp = [[0]*10 for _ in range(N+1)]
    dp[1] = [1]*10
    for i in range(2,N+1):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
            dp[i][j] %= MOD
    print(sum(dp[N])%MOD)

if __name__ == '__main__':
    main()