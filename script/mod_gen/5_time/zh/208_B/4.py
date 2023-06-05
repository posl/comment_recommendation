def countCoin(coinList, value):
    if value == 0:
        return 0
    else:
        minCount = 10000000
        for coin in coinList:
            if coin <= value:
                count = countCoin(coinList, value - coin) + 1
                if count < minCount:
                    minCount = count
        return minCount

if __name__ == '__main__':
    countCoin()