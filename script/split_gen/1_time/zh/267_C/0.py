def get_max_sum(arr, m):
    max_sum = 0
    for i in range(len(arr)-m+1):
        max_sum = max(max_sum, sum([arr[j]*(j+1) for j in range(i, i+m)]))
    return max_sum
