def min_diff(a, b):
    a.sort()
    b.sort()
    i = 0
    j = 0
    min_diff = 10**9
    while i < len(a) and j < len(b):
        if abs(a[i] - b[j]) < min_diff:
            min_diff = abs(a[i] - b[j])
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return min_diff

if __name__ == '__main__':
    min_diff()