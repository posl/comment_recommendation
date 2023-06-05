def median(arr):
    arr.sort()
    if len(arr)%2==0:
        return arr[len(arr)//2]
    else:
        return arr[len(arr)//2+1]
