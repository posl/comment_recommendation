def cal_year(X):
    balance = 100
    year = 0
    while balance < X:
        balance = int(balance * 1.01)
        year += 1
    return year
