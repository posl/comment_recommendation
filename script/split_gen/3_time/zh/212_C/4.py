def get_min_diff(a, b):
    a = sorted(a)
    b = sorted(b)
    i = 0
    j = 0
    min_diff = 1000000000
    while i < len(a) and j < len(b):
        min_diff = min(min_diff, abs(a[i]-b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return min_diff
