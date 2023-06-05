def compare(x,y):
    if x[0] > y[0]:
        return -1
    elif x[0] < y[0]:
        return 1
    else:
        if x[1] < y[1]:
            return -1
        elif x[1] > y[1]:
            return 1
        else:
            return 0
