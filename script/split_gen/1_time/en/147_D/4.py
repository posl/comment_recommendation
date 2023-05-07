def xor_sum(arr):
    xor_sum = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            xor_sum += arr[i]^arr[j]
    return xor_sum
