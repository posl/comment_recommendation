def swap(a, p, q, r, s):
    b = a[0:p-1]
    b.extend(a[r-1:s])
    b.extend(a[q:s])
    b.extend(a[p-1:r-1])
    b.extend(a[s:])
    return b

if __name__ == '__main__':
    swap()