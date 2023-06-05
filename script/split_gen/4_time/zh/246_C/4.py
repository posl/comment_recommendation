def get_min_cost(num, coupon_num, coupon_price, price_list):
    cost = 0
    for price in price_list:
        if coupon_num > 0:
            cost += max(price - coupon_price, 0)
            coupon_num -= 1
        else:
            cost += price
    return cost
