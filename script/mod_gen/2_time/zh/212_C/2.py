def min_diff(a, b):
    a.sort()
    b.sort()
    i = 0
    j = 0
    min_diff = abs(a[0] - b[0])
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            return 0
        elif a[i] < b[j]:
            min_diff = min(min_diff, b[j] - a[i])
            i += 1
        else:
            min_diff = min(min_diff, a[i] - b[j])
            j += 1
    return min_diff

if __name__ == '__main__':
    min_diff()