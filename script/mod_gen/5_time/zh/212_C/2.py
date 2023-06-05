def min_diff(a, b):
    a.sort()
    b.sort()
    min_d = 10 ** 9
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        min_d = min(min_d, abs(a[i] - b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return min_d

if __name__ == '__main__':
    min_diff()