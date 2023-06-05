def getMinNumOfWithdraws(amount):
    # 递归调用
    def getMinNumOfWithdrawsRec(amount, withdraws):
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        minNumOfWithdraws = float('inf')
        for withdraw in withdraws:
            minNumOfWithdraws = min(minNumOfWithdraws, getMinNumOfWithdrawsRec(amount - withdraw, withdraws))
        return minNumOfWithdraws + 1
    withdraws = [1]
    power = 6
    while power <= amount:
        withdraws.append(power)
        power *= 6
    power = 9
    while power <= amount:
        withdraws.append(power)
        power *= 9
    return getMinNumOfWithdrawsRec(amount, withdraws)
