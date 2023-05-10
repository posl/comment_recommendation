def get_min_price(n, k, x, a):
    a.sort()
    price = 0
    for i in range(n):
        if k > 0:
            price += max(a[i]-x, 0)
            k -= 1
        else:
            price += a[i]
    return price

if __name__ == '__main__':
    get_min_price()