def main():
    n, k = map(int, input().split())
    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
    dp[0][0] = 1
    for i in range(1, k+1):
        for j in range(n+1):
            if j >= i:
                dp[i][j] = (dp[i-1][j] + dp[i][j-i]) % (10**9+7)
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[k][n])

if __name__ == '__main__':
    main()