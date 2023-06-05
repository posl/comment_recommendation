def merge(arr):
    arr.sort()
    i = 0
    while i < len(arr) - 1:
        if arr[i][1] >= arr[i+1][0]:
            arr[i][1] = max(arr[i][1], arr[i+1][1])
            arr.pop(i+1)
        else:
            i += 1
    return arr
