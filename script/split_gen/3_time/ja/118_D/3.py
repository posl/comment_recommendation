def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [-1 for _ in range(n + 1)]
    dp[0] = 0
    for i in range(n + 1):
        for j in range(m):
            if i - a[j] >= 0:
                dp[i] = max(dp[i], dp[i - a[j]] + 1)
    ans = ""
    while n > 0:
        for j in range(m):
            if n - a[j] >= 0 and dp[n - a[j]] == dp[n] - 1:
                ans += str(a[j])
                n -= a[j]
                break
    print(ans)
