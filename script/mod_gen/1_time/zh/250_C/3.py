def swap(arr, i):
    tmp = arr[i]
    arr[i] = arr[i+1]
    arr[i+1] = tmp

if __name__ == '__main__':
    swap()