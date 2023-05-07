def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while True:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            if right == mid:
                return mid
            right = mid
        elif arr[mid] < target:
            if left == mid:
                return mid + 1
            left = mid

if __name__ == '__main__':
    binary_search()