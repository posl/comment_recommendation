def main():
    n, k = map(int, input().split())
    mod = 10 ** 9 + 7
    dp = [[0 for j in range(n + 1)] for i in range(k + 1)]
    dp[0][0] = 1
    for i in range(1, k + 1):
        s = 0
        for j in range(n + 1):
            s += dp[i - 1][j]
            s %= mod
            dp[i][j] = s
            if j >= i:
                s -= dp[i - 1][j - i]
                s %= mod
    print(dp[k][n])
