def swap(a, p, q, r, s):
    b = []
    for i in range(len(a)):
        if i >= p-1 and i <= q-1:
            b.append(a[i+r-q])
        elif i >= r-1 and i <= s-1:
            b.append(a[i+q-r])
        else:
            b.append(a[i])
    return b
