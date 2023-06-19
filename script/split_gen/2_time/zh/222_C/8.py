def f(x,y):
    if x==y:
        return 0
    if x=='G':
        if y=='C':
            return 1
        else:
            return -1
    if x=='C':
        if y=='P':
            return 1
        else:
            return -1
    if x=='P':
        if y=='G':
            return 1
        else:
            return -1
    return 0
