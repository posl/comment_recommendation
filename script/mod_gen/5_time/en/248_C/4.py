def main():
    n,m,k = map(int,input().split())
    dp = [[[0]*(k+1) for i in range(m+1)] for j in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(m):
            for l in range(k+1):
                dp[i][j][l] %= 998244353
                dp[i+1][j][l] += dp[i][j][l]
                if l+j+1 <= k:
                    dp[i+1][j+1][l+j+1] += dp[i][j][l]
    ans = 0
    for i in range(m+1):
        ans += dp[n][i][k]
    print(ans%998244353)

if __name__ == '__main__':
    main()