def get_median(arr):
    arr.sort()
    len_arr = len(arr)
    if len_arr % 2 == 0:
        return arr[len_arr//2-1]
    else:
        return arr[len_arr//2]
