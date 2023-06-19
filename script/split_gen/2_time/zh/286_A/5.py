def swap(a, p, q, r, s):
    b = a.copy()
    for i in range(q-p+1):
        b[p+i-1] = a[s+i-1]
    for i in range(s-r+1):
        b[r+i-1] = a[q+i-1]
    return b
