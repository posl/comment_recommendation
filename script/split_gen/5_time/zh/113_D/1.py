def amidakuji(h, w, k):
    if h == 1:
        return 1
    if w == 1:
        if k == 1:
            return 1
        else:
            return 0
    if k == 1:
        return amidakuji(h-1, w-1, 1) + amidakuji(h-1, w, 2)
    elif k == w:
        return amidakuji(h-1, w-1, w-1) + amidakuji(h-1, w, w-2)
    else:
        return amidakuji(h-1, w-1, k-1) + amidakuji(h-1, w, k+1)
