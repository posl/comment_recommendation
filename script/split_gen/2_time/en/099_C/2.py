def main():
    n = int(input())
    dp = [-1] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        dp[i] = dp[i-1] + 1
        for j in range(6, 0, -1):
            if i - j**2 >= 0:
                dp[i] = min(dp[i], dp[i-j**2] + 1)
        for j in range(9, 0, -1):
            if i - j**3 >= 0:
                dp[i] = min(dp[i], dp[i-j**3] + 1)
    print(dp[n])
