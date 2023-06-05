def get_min_money(n, shop_list):
    min_money = -1
    for i in range(n):
        if shop_list[i][2] > 0:
            if min_money == -1 or min_money > shop_list[i][1]:
                min_money = shop_list[i][1]
    return min_money
