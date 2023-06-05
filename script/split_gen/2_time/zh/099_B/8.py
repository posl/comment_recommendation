def get_hight(a, b):
    hight = 0
    for i in range(1, 1000):
        hight += i
        if hight == a:
            hight = i
            break
    return hight
