def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(n + 1):
        for j in range(m):
            if i - a[j] >= 0 and dp[i - a[j]] >= 0:
                dp[i] = max(dp[i], dp[i - a[j]] + 1)
    ans = []
    while n > 0:
        for i in range(m):
            if n - a[i] >= 0 and dp[n - a[i]] == dp[n] - 1:
                ans.append(a[i])
                n -= a[i]
                break
    print(''.join(map(str, ans)))
