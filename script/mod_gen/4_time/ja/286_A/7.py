def swap(arr, a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp
    return arr

if __name__ == '__main__':
    swap()