def get_height(n,m,x,t,d):
    height = t
    for i in range(1,n):
        if i < x:
            height += d
        elif i == x:
            continue
        else:
            height += d
    return height
