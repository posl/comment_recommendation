def min_dif(a, b):
    a.sort()
    b.sort()
    i = 0
    j = 0
    ans = abs(a[i] - b[j])
    while i < len(a) and j < len(b):
        if abs(a[i] - b[j]) < ans:
            ans = abs(a[i] - b[j])
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return ans
