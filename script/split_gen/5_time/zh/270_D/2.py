def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(k):
            if i >= a[j]:
                dp[i] = max(dp[i - a[j]] + a[j], dp[i])
    print(dp[n])
solve()
