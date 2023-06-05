def get_num(arr):
    num = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                num += 1
    return num
