def main():
    N = int(input())
    dp = [N + 1] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            if j ** 6 > i:
                break
            dp[i] = min(dp[i], dp[i - j ** 6] + 1)
        for j in range(1, i + 1):
            if j ** 9 > i:
                break
            dp[i] = min(dp[i], dp[i - j ** 9] + 1)
    print(dp[N])
