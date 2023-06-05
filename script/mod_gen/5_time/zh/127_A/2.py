def cal_fee(age, fee):
    if age > 12:
        return fee
    elif age > 5 and age <= 12:
        return fee // 2
    else:
        return 0

if __name__ == '__main__':
    cal_fee()