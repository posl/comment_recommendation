def main():
    n, m, k = map(int, input().split())
    mod = 998244353
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            for l in range(1, m+1):
                if j-l >= 0:
                    dp[i][j] += dp[i-1][j-l]
                    dp[i][j] %= mod
                else:
                    break
    print(dp[n][k])

if __name__ == '__main__':
    main()