def find_median(array):
    array.sort()
    return array[(len(array)-1)//2]
