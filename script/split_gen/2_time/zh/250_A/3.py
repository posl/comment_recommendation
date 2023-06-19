def getcount(h,w,r,c):
    count = 0
    if r == 1:
        if c == 1:
            count = 2
        elif c == w:
            count = 2
        else:
            count = 3
    elif r == h:
        if c == 1:
            count = 2
        elif c == w:
            count = 2
        else:
            count = 3
    else:
        if c == 1:
            count = 3
        elif c == w:
            count = 3
        else:
            count = 4
    return count
