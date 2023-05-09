def solve():
    n, a, b = map(int, input().split())
    s = input()
    dp = [1e9] * (n + 1)
    dp[0] = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            t = s[i:j]
            dp[j] = min(dp[j], dp[i] + b + (t != t[::-1]) * a)
    print(dp[n])
