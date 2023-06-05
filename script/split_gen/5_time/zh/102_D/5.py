def find_min_diff(a):
    a.sort()
    n = len(a)
    min_diff = 1000000000
    for i in range(0, n-3):
        p = a[i]
        q = a[i+1]
        r = a[n-2]
        s = a[n-1]
        diff = max(p, q, r, s) - min(p, q, r, s)
        if diff < min_diff:
            min_diff = diff
    return min_diff
n = int(input())
a = [int(x) for x in input().split()]
print(find_min_diff(a))
