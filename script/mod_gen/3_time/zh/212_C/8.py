def min_difference(a, b):
    a.sort()
    b.sort()
    i = 0
    j = 0
    min_diff = abs(a[0] - b[0])
    while i < len(a) and j < len(b):
        diff = abs(a[i] - b[j])
        if diff < min_diff:
            min_diff = diff
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return min_diff
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(min_difference(a, b))
