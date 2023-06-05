def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return low
a, b, q = map(int, input().split())
s = [int(input()) for i in range(a)]
t = [int(input()) for i in range(b)]
x = [int(input()) for i in range(q)]
s.sort()
t.sort()
for i in range(q):
    ans = 10 ** 11
    si = binary_search(s, x[i])
    ti = binary_search(t, x[i])
    for ss in [s[si - 1], s[si]]:
        for tt in [t[ti - 1], t[ti]]:
            ans = min(ans, abs(ss - x[i]) + abs(ss - tt), abs(tt - x[i]) + abs(tt - ss))
    print(ans)
