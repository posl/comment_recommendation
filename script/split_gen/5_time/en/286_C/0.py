def solve():
    n, a, b = map(int, input().split())
    s = input()
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(n):
        for j in range(i, n):
            if s[i:j+1] == s[i:j+1][::-1]:
                dp[j+1] = min(dp[j+1], dp[i] + a)
            else:
                dp[j+1] = min(dp[j+1], dp[i] + b)
    print(dp[n])
