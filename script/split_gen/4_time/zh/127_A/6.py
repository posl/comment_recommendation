def calc_fee(age, fee):
    if age <= 5:
        return 0
    elif age <= 12:
        return fee // 2
    else:
        return fee
