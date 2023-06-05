def make_blue(n,x,y):
    if n == 1:
        return 1
    elif n == 2:
        return 0
    else:
        return make_blue(n-1,x,y) + make_red(n-1,x,y) * y
