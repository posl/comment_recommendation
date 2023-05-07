def get_price(a, b):
    price = -1
    for i in range(1, 1000):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            price = i
            break
    return price
