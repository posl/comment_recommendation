def get_kth_value(arr, k):
    arr.sort(reverse=True)
    return arr[k-1]
