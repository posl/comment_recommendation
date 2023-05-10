def swap(i, j, p):
    tmp = p[i]
    p[i] = p[j]
    p[j] = tmp
    return p
