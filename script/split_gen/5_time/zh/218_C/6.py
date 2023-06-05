def rotate90(a):
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0])-1,-1,-1)]
