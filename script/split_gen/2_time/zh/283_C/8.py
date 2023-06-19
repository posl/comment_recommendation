def main():
    s = input()
    n = len(s)
    dp = [0] * (n + 1)
    dp[n] = 0
    dp[n - 1] = 0
    for i in range(n - 2, -1, -1):
        dp[i] = min(dp[i + 1] + int(s[i + 1]), dp[i + 2] + int(s[i + 2]) * 10)
        if i <= n - 3:
            dp[i] = min(dp[i], dp[i + 3] + int(s[i + 3]) * 100)
        dp[i] += 1
    print(dp[0])
