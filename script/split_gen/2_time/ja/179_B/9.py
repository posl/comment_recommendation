def check_zorome(arr):
    count = 1
    for i in range(len(arr)-1):
        if arr[i][0] == arr[i+1][0]:
            count += 1
            if count == 3:
                return True
        else:
            count = 1
    return False
