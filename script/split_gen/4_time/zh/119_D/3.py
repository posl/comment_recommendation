def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return left
A, B, Q = map(int, input().split())
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
x = [int(input()) for _ in range(Q)]
for i in range(Q):
    index_s = binary_search(s, x[i])
    index_t = binary_search(t, x[i])
    ans = 10 ** 11
    for j in [index_s - 1, index_s]:
        for k in [index_t - 1, index_t]:
            d1 = abs(s[j] - x[i]) + abs(t[k] - s[j])
            d2 = abs(t[k] - x[i]) + abs(s[j] - t[k])
            ans = min(ans, d1, d2)
    print(ans)
