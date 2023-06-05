def buy_goods(n, m, a):
    a.sort(reverse=True)
    for i in range(m):
        a[0] = a[0] // 2
        a.sort(reverse=True)
    return sum(a)
