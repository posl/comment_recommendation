def buy_play_snuke(N, shop_list):
    min_price = -1
    for shop in shop_list:
        if shop[2] > 0:
            if min_price == -1:
                min_price = shop[1]
            elif min_price > shop[1]:
                min_price = shop[1]
    return min_price

if __name__ == '__main__':
    buy_play_snuke()