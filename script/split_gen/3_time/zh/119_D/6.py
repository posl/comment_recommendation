def binarySearch(array, target):
    #二分查找
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
A, B, Q = map(int, input().split())
S = [int(input()) for i in range(A)]
T = [int(input()) for i in range(B)]
X = [int(input()) for i in range(Q)]
S.sort()
T.sort()
for i in range(Q):
    ans = 10**19
    x = X[i]
    s = binarySearch(S, x)
    t = binarySearch(T, x)
    for s0 in [S[s-1], S[s]]:
        for t0 in [T[t-1], T[t]]:
            d1 = abs(s0 - x) + abs(t0 - s0)
            d2 = abs(t0 - x) + abs(s0 - t0)
            ans = min(ans, d1, d2)
    print(ans)
