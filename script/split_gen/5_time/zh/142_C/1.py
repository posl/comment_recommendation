def get_order(n, a):
    order = []
    for i in range(n):
        order.append(a.index(i+1)+1)
    return order
