def min_diff(a, b):
    a.sort()
    b.sort()
    min_diff = float('inf')
    i, j = 0, 0
    while i < len(a) and j < len(b):
        min_diff = min(min_diff, abs(a[i] - b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return min_diff
