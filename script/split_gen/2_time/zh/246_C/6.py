def get_min_price(n, k, x, a):
    a.sort()
    price = 0
    for i in range(n):
        if k > 0:
            if a[i] < x:
                price += a[i]
            else:
                price += x
            k -= 1
        else:
            price += a[i]
    return price
