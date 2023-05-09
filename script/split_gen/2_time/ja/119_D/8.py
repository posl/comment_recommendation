def binary_search(arr, target):
    index = 0
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            index = mid
            break
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        index = left
    return index
