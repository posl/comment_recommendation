def search(h, w, a, b):
    if h < w:
        h, w = w, h
    if h == 1 and w == 1:
        return 1
    if a == 0:
        return 1
    if a == 1:
        return h - 1
    if a == 2:
        return 1 + (h - 2) * (w - 1)
    if a == 3:
        return 1 + (h - 2) * (w - 1)

if __name__ == '__main__':
    search()