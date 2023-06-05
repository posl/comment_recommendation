def solve(n, k, l, r):
    mod = 998244353
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(k):
            if i - l[j] >= 1:
                dp[i] += dp[i - l[j]]
                dp[i] %= mod
            if i - r[j] - 1 >= 1:
                dp[i] -= dp[i - r[j] - 1]
                dp[i] %= mod
    return dp[n]
n, k = map(int, input().split())
l = []
r = []
for _ in range(k):
    li, ri = map(int, input().split())
    l.append(li)
    r.append(ri)
print(solve(n, k, l, r))
