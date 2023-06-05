def getCoinCount(money):
    coinCount = 0
    for i in range(10, 0, -1):
        coinCount += money // factorial(i)
        money = money % factorial(i)
    return coinCount
