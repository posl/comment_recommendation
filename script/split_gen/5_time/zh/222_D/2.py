def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    mod = 998244353
    dp = [[0 for i in range(3010)] for j in range(3010)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(a[i], b[i] + 1):
            dp[i + 1][j] = (dp[i + 1][j - 1] + dp[i][j]) % mod
    print(dp[n][b[n - 1]])
