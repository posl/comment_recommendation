def process_query(arr, x, k):
    """
    :param arr: array of integers
    :param x: integer
    :param k: integer
    :return: index of k-th occurrence of x in arr
    """
    count = 0
    for i in range(len(arr)):
        if arr[i] == x:
            count += 1
            if count == k:
                return i+1
    return -1
