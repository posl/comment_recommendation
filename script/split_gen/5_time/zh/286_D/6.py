def pay(x, a, b):
    if x == 0:
        return True
    elif x > 0 and a == 0:
        return False
    else:
        return pay(x - a, a, b - 1) or pay(x, a - 1, b)
