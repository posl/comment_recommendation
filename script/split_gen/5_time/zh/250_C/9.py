def swap(arr, i, j):
    if i == j:
        return
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
