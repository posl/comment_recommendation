def find_kth_number_in_array(arr, x, k):
    if arr.count(x) < k:
        return -1
    else:
        count = 0
        for i in range(0, len(arr)):
            if arr[i] == x:
                count += 1
                if count == k:
                    return i+1
        return -1
