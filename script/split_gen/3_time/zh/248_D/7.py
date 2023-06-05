def count(arr, l, r, x):
    count = 0
    for i in range(l-1, r):
        if arr[i] == x:
            count += 1
    return count
