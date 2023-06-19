def isAllCanBuy(n, x, a):
    for i in range(n):
        if i % 2 == 1:
            a[i] -= 1
    if sum(a) <= x:
        return True
    else:
        return False
