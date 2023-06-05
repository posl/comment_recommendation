def get_hight(a,b):
    if a >= b:
        return -1
    sum = 0
    for i in range(1,1000):
        sum = sum + i
        if sum >= a:
            break
    if sum != a:
        return -1
    sum = 0
    for i in range(1,1000):
        sum = sum + i
        if sum >= b:
            break
    if sum != b:
        return -1
    return b - a
