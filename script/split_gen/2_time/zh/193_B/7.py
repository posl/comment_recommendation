def getMinMoney(n, a, p, x):
    minMoney = -1
    for i in range(n):
        if x[i] > 0:
            money = p[i]
            if minMoney == -1:
                minMoney = money
            else:
                minMoney = min(minMoney, money)
    return minMoney
