def swap(a, b, c, d, e):
    return a[:b-1] + e[c-1:d] + a[b-1:c-1] + e[d:] + a[d:]

if __name__ == '__main__':
    swap()