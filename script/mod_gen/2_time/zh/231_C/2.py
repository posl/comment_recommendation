def binary_search(l, r, x, a):
    if l == r:
        return l
    m = (l + r) // 2
    if a[m] >= x:
        return binary_search(l, m, x, a)
    else:
        return binary_search(m + 1, r, x, a)

if __name__ == '__main__':
    binary_search()