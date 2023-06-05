def min_diff(a, b):
    a.sort()
    b.sort()
    a_len = len(a)
    b_len = len(b)
    i = 0
    j = 0
    min_diff = 2 ** 32
    while i < a_len and j < b_len:
        if a[i] == b[j]:
            return 0
        elif a[i] < b[j]:
            if j > 0:
                min_diff = min(min_diff, b[j] - a[i], a[i] - b[j - 1])
            else:
                min_diff = min(min_diff, b[j] - a[i])
            i += 1
        else:
            if i > 0:
                min_diff = min(min_diff, a[i] - b[j], b[j] - a[i - 1])
            else:
                min_diff = min(min_diff, a[i] - b[j])
            j += 1
    return min_diff

if __name__ == '__main__':
    min_diff()