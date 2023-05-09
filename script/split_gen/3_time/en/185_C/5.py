def main():
    L = int(input())
    dp = [0] * (L + 1)
    dp[0] = 1
    for i in range(1, L + 1):
        for j in range(11):
            if i - (j + 1) >= 0:
                dp[i] += dp[i - (j + 1)]
    print(dp[L])
