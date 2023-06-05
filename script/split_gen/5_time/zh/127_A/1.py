def calcFee(age,fee):
    if age >= 13:
        return fee
    elif age >= 6:
        return fee/2
    else:
        return 0
