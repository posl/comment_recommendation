def solve(n, m, a):
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(m):
            if i - a[j] >= 0 and dp[i - a[j]] != -1:
                dp[i] = max(dp[i], dp[i - a[j]] + 1)
    ans = []
    while n > 0:
        for j in range(m):
            if n - a[j] >= 0 and dp[n - a[j]] == dp[n] - 1:
                ans.append(a[j])
                n -= a[j]
                break
    return ''.join(map(str, ans))
n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))

if __name__ == '__main__':
    solve()