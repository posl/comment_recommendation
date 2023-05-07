def solve():
    n, a, b = map(int, input().split())
    s = input()
    dp = [float("inf")] * (n+1)
    dp[0] = 0
    for i in range(n):
        dp[i+1] = min(dp[i+1], dp[i]+a)
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[j+1] = min(dp[j+1], dp[i]+b)
    print(dp[n])
