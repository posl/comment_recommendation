def main():
    n, k = map(int, input().split())
    mod = 10**9+7
    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
    dp[0][0] = 1
    for i in range(1, k+1):
        for j in range(n+1):
            dp[i][j] = dp[i-1][j]
            if j - i >= 0:
                dp[i][j] += dp[i][j-i]
            dp[i][j] %= mod
    print(dp[k][n])

if __name__ == '__main__':
    main()