def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(amount + 1):
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount]
x = int(input())
coins = [1, 5, 10, 50, 100, 500]
amount = 1000 - x
print(coin_change(coins, amount))
