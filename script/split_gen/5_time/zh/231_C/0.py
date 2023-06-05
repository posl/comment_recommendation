def binary_search(a, n, key):
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if a[mid] == key:
            return mid
        elif key < a[mid]:
            right = mid
        else:
            left = mid + 1
    return -1
n, q = map(int, input().split())
a = list(map(int, input().split()))
x = [int(input()) for _ in range(q)]
a.sort()
for i in x:
    print(binary_search(a, n, i) + 1)
