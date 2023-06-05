def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    return arr

if __name__ == '__main__':
    swap()