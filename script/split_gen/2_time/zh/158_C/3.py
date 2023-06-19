def get_price(a, b):
    for i in range(1, 100):
        if (int(i*1.08) == a) and (int(i*1.1) == b):
            return i
    return -1
