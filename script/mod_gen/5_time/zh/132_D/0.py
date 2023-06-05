def main():
    n,k = map(int, input().split())
    mod = 10**9 + 7
    dp = [[0 for i in range(n+1)] for j in range(k+1)]
    dp[0][0] = 1
    for i in range(1,k+1):
        for j in range(n+1):
            if j < i:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i][j-1] * (i+1)) % mod
    print(dp[k][n])

if __name__ == '__main__':
    main()