def calc_price(n, price_list):
    price_list.sort()
    price_list[-1] = price_list[-1] / 2
    return sum(price_list)

if __name__ == '__main__':
    calc_price()