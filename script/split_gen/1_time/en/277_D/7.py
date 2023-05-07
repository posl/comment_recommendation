def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != 0:
        print(sum(a))
        return
    for i in range(n):
        if a[i] != 0:
            a = a[i:]
            break
    n = len(a)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        dp[i][i + 1] = a[i]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n + 1):
            if j - i == 1:
                dp[i][j] = a[i]
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + a[i]
    ans = 0
    for i in range(n + 1):
        if (dp[0][i] + i) % m != 0:
            ans = max(ans, dp[0][i] + i)
    print(ans)
