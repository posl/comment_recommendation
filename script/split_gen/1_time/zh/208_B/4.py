def min_coins(p):
    coins = [1]
    for i in range(1, 11):
        coins.append(coins[i-1] * i)
    count = 0
    for i in range(10, 0, -1):
        count += p // coins[i]
        p = p % coins[i]
    return count
