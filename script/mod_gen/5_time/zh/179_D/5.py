def solve(n, k, l, r):
    ans = 0
    dp = [0 for _ in range(n + 1)]
    dp[1] = 1
    for i in range(1, n + 1):
        for j in range(k):
            if i + l[j] <= n:
                dp[i + l[j]] += dp[i]
                dp[i + l[j]] %= 998244353
            if i + r[j] + 1 <= n:
                dp[i + r[j] + 1] -= dp[i]
                dp[i + r[j] + 1] %= 998244353
    for i in range(1, n + 1):
        dp[i] += dp[i - 1]
        dp[i] %= 998244353
    return dp[n]
n, k = map(int, input().split())
l = []
r = []
for i in range(k):
    a, b = map(int, input().split())
    l.append(a)
    r.append(b)
print(solve(n, k, l, r))
