def buy_play_snuke(n, shop_list):
    min_cost = -1
    for shop in shop_list:
        shop_cost = shop[1]
        shop_stock = shop[2]
        shop_walk_time = shop[0]
        if shop_stock > 0:
            if min_cost == -1:
                min_cost = shop_cost
            else:
                if shop_cost < min_cost:
                    min_cost = shop_cost
    return min_cost

if __name__ == '__main__':
    buy_play_snuke()