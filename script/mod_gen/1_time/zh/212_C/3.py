def min_diff(a, b):
    a.sort()
    b.sort()
    min_diff = 10**10
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            return 0
        if a[i] < b[j]:
            min_diff = min(min_diff, b[j] - a[i])
            i += 1
        else:
            min_diff = min(min_diff, a[i] - b[j])
            j += 1
    return min_diff

if __name__ == '__main__':
    min_diff()