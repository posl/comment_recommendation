def findMinNum(n, arr):
    arr.sort()
    if arr[0] > 0:
        return 0
    if arr[-1] < 0:
        return 0
    for i in range(n-1):
        if arr[i] >= 0:
            if arr[i+1] - arr[i] > 1:
                return arr[i] + 1
    return arr[-1] + 1
