def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * 10
    for i in range(10):
        dp = [[0] * 10 for _ in range(n + 1)]
        dp[0][a[0]] = 1
        for j in range(n - 1):
            for k in range(10):
                val = (k + a[j + 1]) % 10
                dp[j + 1][val] += dp[j][k]
                dp[j + 1][val] %= 998244353
                val = (k * a[j + 1]) % 10
                dp[j + 1][val] += dp[j][k]
                dp[j + 1][val] %= 998244353
        ans[i] = dp[n - 1][i]
    for i in range(10):
        print(ans[i])
