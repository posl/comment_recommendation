def main():
    n, m, k = map(int, input().split())
    dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            for s in range(1, k+1):
                dp[i][j][s] += dp[i-1][j][s]
                if s - j >= 1:
                    dp[i][j][s] += dp[i-1][j][s-j]
                dp[i][j][s] %= 998244353
    ans = 0
    for j in range(1, m+1):
        ans += dp[n][j][k]
        ans %= 998244353
    print(ans)

if __name__ == '__main__':
    main()