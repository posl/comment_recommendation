def swap(a, p, q, r, s):
    b = []
    for i in range(p-1):
        b.append(a[i])
    for i in range(r-1, s):
        b.append(a[i])
    for i in range(q, r-1):
        b.append(a[i])
    for i in range(s, len(a)):
        b.append(a[i])
    return b
