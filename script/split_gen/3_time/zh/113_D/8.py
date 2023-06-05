def amidakuji(h, w, k):
    if w == 1:
        return 1
    if k == 1:
        return amidakuji(h - 1, w - 1, k) + amidakuji(h - 1, w, k + 1)
    if k == w:
        return amidakuji(h - 1, w - 1, k - 1) + amidakuji(h - 1, w, k)
    return amidakuji(h - 1, w - 1, k - 1) + amidakuji(h - 1, w - 1, k) + amidakuji(h - 1, w - 1, k + 1)
h, w, k = map(int, input().split())
print(amidakuji(h, w, k) % 1000000007)
