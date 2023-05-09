def can_pay(x, a, b):
    if x == 0:
        return True
    if x < 0 or len(a) == 0:
        return False
    for i in range(0, b[0] + 1):
        if can_pay(x - a[0] * i, a[1:], b[1:]):
            return True
    return False
