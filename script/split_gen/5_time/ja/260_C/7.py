def count_blue(n,x,y):
    if n == 1:
        return 1
    else:
        return count_blue(n-1,x,y) + count_red(n-1,x,y)
