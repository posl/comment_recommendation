def canpay(x, a, b):
    if x == 0:
        return True
    elif x < 0 or len(a) == 0 or len(b) == 0:
        return False
    else:
        for i in range(b[0]+1):
            if canpay(x-a[0]*i, a[1:], b[1:]):
                return True
        return False
