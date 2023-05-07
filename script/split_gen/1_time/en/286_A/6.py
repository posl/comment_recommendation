def swap_sequence(a, p, q, r, s):
    b = a.copy()
    for i in range(p, q+1):
        b[i-1] = a[s-i+r-2]
    for i in range(r, s+1):
        b[i-1] = a[q-i+p-2]
    return b
