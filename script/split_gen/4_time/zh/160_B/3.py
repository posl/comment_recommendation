def calc_happiness(X):
    # 500円硬貨
    n_500 = X // 500
    X -= n_500 * 500
    # 5円硬貨
    n_5 = X // 5
    return n_500 * 1000 + n_5 * 5
