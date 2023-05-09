def swap_array(a, p, q, r, s):
    b = a[:p]
    b.extend(a[r:s+1])
    b.extend(a[q+1:r])
    b.extend(a[p:q+1])
    b.extend(a[s+1:])
    return b
