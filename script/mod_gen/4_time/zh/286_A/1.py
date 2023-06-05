def swap(a, p, q, r, s):
    b = a[p-1:q] + a[r-1:s] + a[q:r-1] + a[s:]
    return b

if __name__ == '__main__':
    swap()