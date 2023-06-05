def get_min_price(n, shops):
    min_price = -1
    for i in range(n):
        if shops[i][2] > 0:
            if min_price == -1:
                min_price = shops[i][1]
            else:
                min_price = min(min_price, shops[i][1])
    return min_price
