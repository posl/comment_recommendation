def isPayable(coinList, value):
    if value == 0:
        return True
    elif len(coinList) == 0:
        return False
    else:
        for i in range(0, coinList[0][1]+1):
            if value >= i*coinList[0][0]:
                if isPayable(coinList[1:], value - i*coinList[0][0]):
                    return True
        return False
