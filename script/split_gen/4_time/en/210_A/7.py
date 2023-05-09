def calculate_cabbage_price(cabbage_count, cabbage_discount_count, cabbage_price, cabbage_discount_price):
    if cabbage_count > cabbage_discount_count:
        return (cabbage_discount_count * cabbage_price) + ((cabbage_count - cabbage_discount_count) * cabbage_discount_price)
    else:
        return cabbage_count * cabbage_price
