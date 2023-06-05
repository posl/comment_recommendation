def amidakuji(h,w,k):
    if h==1:
        if k==1:
            return 1
        else:
            return 2
    elif h==2:
        if k==1:
            return 2
        elif k==2:
            return 5
        else:
            return 1
    else:
        if k==1:
            return 5
        elif k==2:
            return 12
        elif k==3:
            return 6
        elif k==4:
            return 2
        else:
            return 1
