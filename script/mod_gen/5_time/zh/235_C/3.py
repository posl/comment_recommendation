def get_index(arr, x, k):
    count = 0
    for i in range(len(arr)):
        if arr[i] == x:
            count += 1
            if count == k:
                return i + 1
    return -1

if __name__ == '__main__':
    get_index()