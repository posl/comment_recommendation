def main():
    n, m, k = map(int, input().split())
    dp = [[[0] * (k + 1) for i in range(m + 1)] for j in range(n + 1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(m + 1):
            for s in range(k + 1):
                if dp[i][j][s] == 0:
                    continue
                for a in range(1, m + 1):
                    if s + a > k:
                        break
                    dp[i + 1][a][s + a] += dp[i][j][s]
                    dp[i + 1][a][s + a] %= 998244353
    ans = 0
    for j in range(m + 1):
        ans += dp[n][j][k]
        ans %= 998244353
    print(ans)
