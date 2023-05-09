def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    s = sum(a)
    mod = 998244353
    dp = [[0 for i in range(s+1)] for j in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(s+1):
            dp[i+1][j] += dp[i][j]
            dp[i+1][j] %= mod
            if j + a[i] <= s:
                dp[i+1][j+a[i]] += dp[i][j]
                dp[i+1][j+a[i]] %= mod
    ans = 0
    for i in range(1,s+1):
        if i * n % s == 0:
            ans += dp[n][i]
            ans %= mod
    print(ans)
