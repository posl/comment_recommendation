def get_min_price(n, k, x, a):
    min_price = 0
    for i in range(n):
        if a[i] > x:
            min_price += a[i] - x
        else:
            min_price += 0
    return min_price

if __name__ == '__main__':
    get_min_price()