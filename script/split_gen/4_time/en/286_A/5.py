def swap(a, p, q, r, s):
    b = a[:]
    for i in range(p-1, q):
        b[i] = a[r-1+i-q]
    for i in range(r-1, s):
        b[i] = a[p-1+i-r]
    return b
