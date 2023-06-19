def find_closest_num(num, arr):
    arr.sort()
    # print(arr)
    if num < arr[0]:
        return arr[0]
    if num > arr[-1]:
        return arr[-1]
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == num:
            return arr[mid]
        elif arr[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    if arr[low] - num < num - arr[high]:
        return arr[low]
    else:
        return arr[high]

if __name__ == '__main__':
    find_closest_num()