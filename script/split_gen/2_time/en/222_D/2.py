def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mod = 998244353
    dp = [[0 for _ in range(3001)] for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(3001):
            if a[i] <= j <= b[i]:
                dp[i + 1][j] = dp[i][j]
            dp[i + 1][j] += dp[i + 1][j - 1]
            dp[i + 1][j] %= mod
    print(dp[n][3000])
