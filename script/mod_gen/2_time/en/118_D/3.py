def solve(n, m, a):
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(n + 1):
        if dp[i] == -1:
            continue
        for j in range(m):
            if i + a[j] <= n:
                dp[i + a[j]] = max(dp[i + a[j]], dp[i] * 10 + a[j])
    return dp[n]
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
a = [2, 5, 5, 4, 5, 6, 3, 7, 6]
n = 20
m = 9
print(solve(n, m, a))
