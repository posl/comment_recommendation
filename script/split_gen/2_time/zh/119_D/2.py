def find_nearest(arr, x):
    n = len(arr)
    if x <= arr[0]:
        return arr[0]
    if x >= arr[n-1]:
        return arr[n-1]
    i = 0
    j = n
    mid = 0
    while i < j:
        mid = (i+j)//2
        if arr[mid] == x:
            return arr[mid]
        if x < arr[mid]:
            if mid > 0 and x > arr[mid-1]:
                return get_closest(arr[mid-1], arr[mid], x)
            j = mid
        else:
            if mid < n-1 and x < arr[mid+1]:
                return get_closest(arr[mid], arr[mid+1], x)
            i = mid + 1
    return arr[mid]
