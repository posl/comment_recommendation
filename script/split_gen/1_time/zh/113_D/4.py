def amidakuji(h, w, k):
    if h == 1:
        return 1
    if k == 1:
        return amidakuji(h-1, w, k) + amidakuji(h-1, w, k+1)
    if k == w:
        return amidakuji(h-1, w, k-1) + amidakuji(h-1, w, k)
    return amidakuji(h-1, w, k-1) + amidakuji(h-1, w, k) + amidakuji(h-1, w, k+1)
