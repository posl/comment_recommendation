def main():
    N = int(input())
    mod = 998244353
    dp = [[0 for _ in range(10)] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N+1):
        for j in range(10):
            for k in range(10):
                if abs(j-k) <= 1:
                    dp[i][j] += dp[i-1][k]
                    dp[i][j] %= mod
    ans = 0
    for i in range(10):
        ans += dp[N][i]
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()