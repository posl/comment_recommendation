def judgeStar(n, a, b):
    aCount = {}
    bCount = {}
    for i in range(n-1):
        aCount[a[i]] = 0
        bCount[b[i]] = 0
    for i in range(n-1):
        aCount[a[i]] += 1
        bCount[b[i]] += 1
    for i in range(n-1):
        if aCount[a[i]] > 1 or bCount[b[i]] > 1:
            return False
    return True
