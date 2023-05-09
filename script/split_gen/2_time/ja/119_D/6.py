def binary_search(array, target):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid, target
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left, array[left]
A, B, Q = map(int, input().split())
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
x = [int(input()) for _ in range(Q)]
for i in range(Q):
    idx_s, val_s = binary_search(s, x[i])
    idx_t, val_t = binary_search(t, x[i])
    if idx_s == 0:
        if idx_t == 0:
            print(max(val_s, val_t) - x[i])
        else:
            print(max(val_s, val_t) - min(val_t, x[i]))
    elif idx_t == 0:
        print(max(val_s, val_t) - min(val_s, x[i]))
    else:
        print(max(val_s, val_t) - max(min(val_s, x[i]), min(val_t, x[i])))
