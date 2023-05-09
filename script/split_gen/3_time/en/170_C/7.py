def nearestXor(x, n, p):
    if n == 0:
        return x
    p = set(p)
    if x not in p:
        return x
    for i in range(1, 101):
        if x - i not in p:
            return x - i
        if x + i not in p:
            return x + i
