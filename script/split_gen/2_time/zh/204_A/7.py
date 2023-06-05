def getMedian(a, k):
    n = len(a)
    b = []
    for i in range(n-k+1):
        for j in range(n-k+1):
            c = []
            for x in range(k):
                for y in range(k):
                    c.append(a[i+x][j+y])
            c.sort()
            b.append(c[(k*k)//2])
    b.sort()
    return b[0]
