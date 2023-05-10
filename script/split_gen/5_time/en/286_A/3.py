def swap(a, p, q, r, s):
    b = a[:p-1]
    b.extend(a[r-1:s])
    b.extend(a[q:s])
    b.extend(a[p-1:q])
    b.extend(a[s:])
    return b
