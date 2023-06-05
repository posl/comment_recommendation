def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    MOD = 998244353
    # dp[i][j] = C[i][j] * dp[i-1][j]
    dp = [[0 for _ in range(3001)] for _ in range(3001)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(3001):
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= MOD
            if j >= a[i]:
                dp[i+1][j] += dp[i][j-a[i]]
                dp[i+1][j] %= MOD
            if j >= b[i]:
                dp[i+1][j] -= dp[i][j-b[i]-1]
                dp[i+1][j] %= MOD
    print(dp[n][3000])

if __name__ == '__main__':
    main()