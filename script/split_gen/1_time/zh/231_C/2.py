def binary_search(a, x):
    """二分查找"""
    n = len(a)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
n, q = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)
for _ in range(q):
    x = int(input())
    print(binary_search(a, x) + 1)
