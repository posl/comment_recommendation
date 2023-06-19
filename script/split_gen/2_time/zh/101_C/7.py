def calc(a, k):
    n = len(a)
    count = 0
    for i in range(n-k+1):
        m = min(a[i:i+k])
        for j in range(i, i+k):
            a[j] = m
        count += 1
    return count
