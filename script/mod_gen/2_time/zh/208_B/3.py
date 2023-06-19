def get_coin_count(coin_list, price):
    coin_count = 0
    for coin in coin_list[::-1]:
        coin_count += price // coin
        price %= coin
    return coin_count

if __name__ == '__main__':
    get_coin_count()