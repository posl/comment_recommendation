def max_diff(arr):
    max = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if abs(arr[i]-arr[j])>max:
                max = abs(arr[i]-arr[j])
    return max
