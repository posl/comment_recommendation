def swap_array(a, p, q, r, s):
    b = a.copy()
    b[p-1:q] = a[r-1:s]
    b[r-1:s] = a[p-1:q]
    return b
