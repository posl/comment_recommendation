def binary_search(array, x):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return left
n, q = map(int, input().split())
a = list(map(int, input().split()))
x = [int(input()) for _ in range(q)]
a.sort()
for i in range(q):
    print(n - binary_search(a, x[i]))
