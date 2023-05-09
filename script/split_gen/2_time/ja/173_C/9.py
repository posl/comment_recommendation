def check(a, h, w, k):
    ret = 0
    for i in range(h):
        for j in range(w):
            if a[i][j] == '#':
                ret += 1
    return ret == k
