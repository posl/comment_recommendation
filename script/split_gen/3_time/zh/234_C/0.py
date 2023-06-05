def getKthNumber(k):
    if k == 1:
        return 2
    elif k == 2:
        return 20
    elif k == 3:
        return 22
    else:
        k -= 3
        num = 24
        while k > 0:
            num += 2
            if isOK(num):
                k -= 1
        return num
