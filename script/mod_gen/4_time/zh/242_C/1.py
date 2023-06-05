def main():
    N = int(input())
    mod = 998244353
    dp = [[0 for _ in range(10)] for _ in range(N+1)]
    for i in range(1,10):
        dp[1][i] = 1
    for i in range(2,N+1):
        for j in range(0,10):
            if j > 0:
                dp[i][j] += dp[i-1][j-1]
            if j < 9:
                dp[i][j] += dp[i-1][j+1]
            dp[i][j] %= mod
    ans = 0
    for i in range(0,10):
        ans += dp[N][i]
    print(ans%mod)

if __name__ == '__main__':
    main()