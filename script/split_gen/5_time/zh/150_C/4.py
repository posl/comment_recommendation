def getNum(a):
    n = len(a)
    if n == 1:
        return 0
    else:
        b = a[1:]
        c = []
        for i in range(len(b)):
            if a[0] > b[i]:
                c.append(b[i])
        return getNum(c) + len(c)
