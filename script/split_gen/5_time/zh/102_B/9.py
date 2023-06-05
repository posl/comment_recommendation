def get_max_diff(arr):
    max = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            diff = abs(arr[i]-arr[j])
            if diff > max:
                max = diff
    return max
