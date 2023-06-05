def get_extra_coin_num(coin_num):
    return 100 - coin_num % 100

if __name__ == '__main__':
    get_extra_coin_num()