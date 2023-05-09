def swap(a, p, q, r, s):
    b = a[0:p-1] + a[r-1:s] + a[q:s] + a[p-1:q-1] + a[s:]
    return b

if __name__ == '__main__':
    swap()