def main():
    n = int(input())
    coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    dp = [10000000 for i in range(n + 1)]
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(10):
            if i - coins[j] >= 0:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    print(dp[n])
