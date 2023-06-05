def swap(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left = left + 1
        right = right - 1
