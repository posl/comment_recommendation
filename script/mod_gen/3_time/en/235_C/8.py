def find_kth_occurrence(arr, k, x):
    count = 0
    for i in range(len(arr)):
        if arr[i] == x:
            count += 1
            if count == k:
                return i+1
    return -1

if __name__ == '__main__':
    find_kth_occurrence()