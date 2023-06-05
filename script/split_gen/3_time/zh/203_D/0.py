def get_median(x, y, k, n, a):
    l = []
    for i in range(k):
        for j in range(k):
            l.append(a[x+i][y+j])
    l.sort()
    return l[(k*k)//2]
