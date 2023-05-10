def binary_search(arr, x, k):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            right = mid - 1
        else:
            if mid == k - 1:
                return mid
            elif mid > k - 1:
                right = mid - 1
            else:
                left = mid + 1
    return -1
n, q = map(int,input().split())
a = list(map(int,input().split()))
for _ in range(q):
    x, k = map(int,input().split())
    print(binary_search(a, x, k) + 1)

if __name__ == '__main__':
    binary_search()