def get_max_sum(arr):
    n = len(arr)
    if n == 2:
        return arr[0] + arr[1]
    sum = arr[0] + arr[1]
    for i in range(1, n-1):
        if arr[i] > arr[i-1]:
            sum += arr[i]
        else:
            sum += arr[i-1]
    sum += arr[-1]
    return sum
