def minDiff(a, b):
    a.sort()
    b.sort()
    i, j = 0, 0
    minDiff = 2 * 10**9
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            minDiff = min(minDiff, b[j] - a[i])
            i += 1
        elif a[i] > b[j]:
            minDiff = min(minDiff, a[i] - b[j])
            j += 1
        else:
            minDiff = 0
            break
    return minDiff
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(minDiff(a, b))
