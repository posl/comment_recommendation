def swap(arr, p, q, r, s):
    arr1 = arr[:p]
    arr2 = arr[p:q]
    arr3 = arr[q:r]
    arr4 = arr[r:s]
    arr5 = arr[s:]
    arr = arr1 + arr4 + arr3 + arr2 + arr5
    return arr
