def main():
    L = int(input())
    dp = [0] * (L + 1)
    dp[0] = 1
    for i in range(1, L + 1):
        for j in range(1, min(i, 12) + 1):
            dp[i] += dp[i - j]
    print(dp[L])
