def main():
    n, m, k = map(int, input().split())
    dp = [[[0 for _ in range(k+1)] for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(m+1):
            for l in range(k+1):
                for a in range(j, m+1):
                    if l + a <= k:
                        dp[i+1][a][l+a] += dp[i][j][l]
                        dp[i+1][a][l+a] %= 998244353
    print(sum(dp[n][j][k] for j in range(m+1)) % 998244353)

if __name__ == '__main__':
    main()