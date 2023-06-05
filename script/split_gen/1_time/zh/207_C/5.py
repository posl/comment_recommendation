def func(l,r):
    if l[0]==1:
        if r[0]==1:
            return 1
        elif r[0]==2:
            return 1
        elif r[0]==3:
            return 0
        else:
            return 0
    elif l[0]==2:
        if r[0]==1:
            return 1
        elif r[0]==2:
            return 1
        elif r[0]==3:
            return 1
        else:
            return 0
    elif l[0]==3:
        if r[0]==1:
            return 0
        elif r[0]==2:
            return 1
        elif r[0]==3:
            return 1
        else:
            return 0
    else:
        if r[0]==1:
            return 0
        elif r[0]==2:
            return 0
        elif r[0]==3:
            return 0
        else:
            return 0
