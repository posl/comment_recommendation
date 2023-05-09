def calc_fee(age, fee):
    if age >= 13:
        return fee
    elif age >= 6 and age <= 12:
        return int(fee / 2)
    else:
        return 0
