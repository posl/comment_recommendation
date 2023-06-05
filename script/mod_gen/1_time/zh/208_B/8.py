def getCoins():
    p = int(input())
    coins = [1]
    for i in range(2, 11):
        coins.append(coins[-1] * i)
    count = 0
    while p > 0:
        for i in range(9, -1, -1):
            if p >= coins[i]:
                p -= coins[i]
                count += 1
                break
    print(count)
getCoins()
