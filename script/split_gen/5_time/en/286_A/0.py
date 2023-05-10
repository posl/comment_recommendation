def swap(a, p, q, r, s):
    b = a[:p] + a[r:s+1] + a[q+1:r] + a[p:q+1] + a[s+1:]
    return b
