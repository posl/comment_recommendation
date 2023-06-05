def getMinCoins(p):
    # 硬币的种类
    coins = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    # 从大到小排序
    coins.reverse()
    # 硬币的数量
    count = 0
    for coin in coins:
        # 硬币的数量
        coinCount = p // coin
        count += coinCount
        # 剩余的钱
        p -= coin * coinCount
    return count

if __name__ == '__main__':
    getMinCoins()