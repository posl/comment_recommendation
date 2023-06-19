def get_median(arr):
    arr.sort()
    length = len(arr)
    if length % 2 == 1:
        return arr[length//2]
    else:
        return arr[length//2-1]
