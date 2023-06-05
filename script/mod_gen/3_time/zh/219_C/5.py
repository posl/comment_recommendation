def cmp(x, y):
    if x[1] < y[1]:
        return -1
    elif x[1] == y[1]:
        if x[0] < y[0]:
            return -1
        else:
            return 1
    else:
        return 1

if __name__ == '__main__':
    cmp()