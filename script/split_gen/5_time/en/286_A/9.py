def swap_list(a, start, end):
    b = a[start:end]
    a[start:end] = b[::-1]
    return a
