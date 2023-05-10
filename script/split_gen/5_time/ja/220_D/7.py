def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        dp = [[0] * 10 for _ in range(n)]
        for j in range(10):
            dp[0][(j + a[0]) % 10] += 1
            dp[0][(j * a[0]) % 10] += 1
        for j in range(1, n):
            for k in range(10):
                dp[j][(k + a[j]) % 10] += dp[j - 1][k]
                dp[j][(k + a[j]) % 10] %= mod
                dp[j][(k * a[j]) % 10] += dp[j - 1][k]
                dp[j][(k * a[j]) % 10] %= mod
        ans[i] = dp[-1][i]
    print(*ans, sep="\n")
