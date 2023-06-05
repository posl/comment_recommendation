def get_next_prize_coin_num(coin_num):
    if coin_num % 100 == 0:
        return 100
    else:
        return 100 - (coin_num % 100)
