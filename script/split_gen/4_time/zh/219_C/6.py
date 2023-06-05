def get_order_dict(order):
    order_dict = {}
    for i in range(len(order)):
        order_dict[order[i]] = i
    return order_dict
