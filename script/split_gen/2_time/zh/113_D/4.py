def amidakuji(h,w,k):
    if w == 1:
        return 1
    elif k == 1:
        return amidakuji(h-1,w-1,1)
    elif k == w:
        return amidakuji(h-1,w-1,w-1)
    else:
        return amidakuji(h-1,w-1,k-1) + amidakuji(h-1,w-1,k)
