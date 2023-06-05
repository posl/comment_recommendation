def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, r, x)
    else:
        return -1
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
for i in range(Q):
    L, R, X = map(int, input().split())
    print(binary_search(A, L - 1, R - 1, X))
