def get_price(age, price):
    if age >= 13:
        return price
    elif age >= 6:
        return int(price / 2)
    else:
        return 0
