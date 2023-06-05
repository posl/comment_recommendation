def binarySearch(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return low
A, B, Q = [int(x) for x in input().split()]
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
x = [int(input()) for _ in range(Q)]
s.sort()
t.sort()
for i in range(Q):
    si = binarySearch(s, x[i])
    ti = binarySearch(t, x[i])
    ans = 10 ** 12
    for ss in [s[si - 1], s[si]]:
        for tt in [t[ti - 1], t[ti]]:
            d1 = abs(ss - x[i]) + abs(tt - ss)
            d2 = abs(tt - x[i]) + abs(ss - tt)
            ans = min(ans, d1, d2)
    print(ans)

if __name__ == '__main__':
    binarySearch()