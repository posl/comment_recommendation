def main():
    L = int(input())
    dp = [0] * (L + 1)
    dp[0] = 1
    for i in range(1, L + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]
    print(dp[L])
