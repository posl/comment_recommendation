def get_area(t,l,r):
    if t == 1:
        return [l,r]
    elif t == 2:
        return [l,r-1]
    elif t == 3:
        return [l+1,r]
    else:
        return [l+1,r-1]
