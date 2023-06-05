def median(arr):
    arr.sort()
    mid = len(arr) // 2
    return arr[mid] if len(arr) % 2 != 0 else (arr[mid] + arr[mid - 1]) / 2
