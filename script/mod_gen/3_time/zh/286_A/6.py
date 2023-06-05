def swap(a, b, c, d, e):
    return a[d:e] + a[b:c] + a[a:b] + a[c:d] + a[e:]

if __name__ == '__main__':
    swap()