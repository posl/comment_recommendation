def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mod = 998244353
    dp = [[0 for _ in range(3001)] for _ in range(3001)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(a[i], b[i] + 1):
            for k in range(j + 1):
                dp[i + 1][k] += dp[i][k]
                dp[i + 1][k] %= mod
            for k in range(j, -1, -1):
                dp[i + 1][j] += dp[i][k]
                dp[i + 1][j] %= mod
    print(sum(dp[n]) % mod)
