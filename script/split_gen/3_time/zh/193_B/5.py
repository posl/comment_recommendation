def get_min_money(n, stores):
    min_money = -1
    for i in range(n):
        if stores[i][2] > 0:
            if min_money == -1 or min_money > stores[i][1]:
                min_money = stores[i][1]
    return min_money
