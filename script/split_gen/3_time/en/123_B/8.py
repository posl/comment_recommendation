def calculate_wait_time(orders):
    max_time = 0
    for order in orders:
        order_time = (order // 10 + 1) * 10
        if order_time > max_time:
            max_time = order_time
    return max_time
