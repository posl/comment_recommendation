def find_first_missing_positive_integer(arr):
    for i in range(0, len(arr)):
        while arr[i] >= 0 and arr[i] < len(arr) and arr[i] != arr[arr[i]]:
            temp = arr[i]
            arr[i] = arr[arr[i]]
            arr[temp] = temp
    for i in range(0, len(arr)):
        if arr[i] != i:
            return i
    return len(arr)

if __name__ == '__main__':
    find_first_missing_positive_integer()