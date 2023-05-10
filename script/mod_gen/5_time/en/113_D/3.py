def main():
    h,w,k = map(int, input().split())
    dp = [[0 for _ in range(w+1)] for _ in range(h+1)]
    dp[0][1] = 1
    for i in range(1, h+1):
        for j in range(1, w+1):
            dp[i][j] = dp[i-1][j-1] * dp[i-1][j] % 1000000007
            dp[i][j] += dp[i-1][j] * dp[i-1][j+1] % 1000000007
            dp[i][j] += dp[i-1][j] * dp[i-1][j-1] % 1000000007
            dp[i][j] %= 1000000007
    print(dp[h][k])

if __name__ == '__main__':
    main()