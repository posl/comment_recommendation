def buy_goods(n, m, a):
    a.sort()
    cost = 0
    for i in range(n):
        cost += a[i]
    for i in range(m):
        cost = cost / 2
    return int(cost)
