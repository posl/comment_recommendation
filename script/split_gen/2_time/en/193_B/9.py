def buy_play_snuke(n, shops):
    min_price = -1
    for shop in shops:
        if shop[2] > 0:
            if min_price == -1:
                min_price = shop[1]
            else:
                min_price = min(min_price, shop[1])
    return min_price
