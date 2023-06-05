def find_kth_min(a, k):
    if k > a[-1]:
        return a[-1] + k - a[-1]
    if k < a[0]:
        return k
    l = 0
    r = len(a) - 1
    while l < r:
        m = (l + r) // 2
        if a[m] < k:
            l = m + 1
        else:
            r = m
    return a[l] + k - a[l]
