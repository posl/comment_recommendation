def getMinDiff(a,b):
    a.sort()
    b.sort()
    min_diff = abs(a[0] - b[0])
    for i in range(len(a)):
        for j in range(len(b)):
            if abs(a[i] - b[j]) < min_diff:
                min_diff = abs(a[i] - b[j])
    return min_diff
