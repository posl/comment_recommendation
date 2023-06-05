def get_min(a, x, k):
    if k > 5:
        return -1
    count = 0
    for i in range(len(a)):
        if a[i] >= x:
            count += 1
            if count == k:
                return a[i]
    return -1
