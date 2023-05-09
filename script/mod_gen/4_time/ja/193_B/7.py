def calc_min_price(n, a_list, p_list, x_list):
    min_price = -1
    for i in range(n):
        if x_list[i] > 0:
            if min_price == -1:
                min_price = p_list[i]
            else:
                min_price = min(min_price, p_list[i])
    return min_price

if __name__ == '__main__':
    calc_min_price()