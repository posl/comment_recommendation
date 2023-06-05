def swap(a, b, c, d, e):
    return a[d:e] + a[b:c] + a[a:b] + a[c:d] + a[e:]
