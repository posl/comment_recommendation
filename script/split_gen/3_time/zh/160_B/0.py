def get_coin_num(x):
    coin_num = 0
    coin_num += x // 500 * 1000
    x = x % 500
    coin_num += x // 5 * 5
    return coin_num
