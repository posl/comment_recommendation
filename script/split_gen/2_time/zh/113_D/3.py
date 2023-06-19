def amidakuji(h,w,k):
    if h==1:
        return 1
    elif w==1:
        return 2
    elif k==1:
        return 2**(w-1)
    elif k==w:
        return 2**(w-1)
    else:
        return 2**(w-2)
