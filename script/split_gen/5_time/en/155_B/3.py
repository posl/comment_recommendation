def check_divisibility_by_3_or_5(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            if arr[i] % 3 != 0 and arr[i] % 5 != 0:
                return "DENIED"
    return "APPROVED"
