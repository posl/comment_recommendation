def get_min_price(n, m, price_list):
    price_list.sort(key=lambda x:x[0])
    total_num = 0
    min_price = 0
    for price in price_list:
        if total_num + price[1] < m:
            total_num += price[1]
            min_price += price[0] * price[1]
        else:
            min_price += price[0] * (m - total_num)
            break
    return min_price
