def amidakuji(h,w,k):
    if w == 1:
        return 1
    if k == 1:
        return amidakuji(h,w-1,k)
    if k == w:
        return amidakuji(h,w-1,k-1)
    return amidakuji(h,w-1,k-1) + amidakuji(h,w-1,k)
