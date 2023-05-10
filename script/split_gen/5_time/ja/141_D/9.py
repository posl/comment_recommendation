def calc_price(price, discount_ticket):
    if discount_ticket == 0:
        return price
    else:
        return int(price / (2 ** discount_ticket))
