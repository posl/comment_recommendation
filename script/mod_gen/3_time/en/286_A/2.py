def swap(arr, p, q, r, s):
    arr[p-1:q], arr[r-1:s] = arr[r-1:s], arr[p-1:q]
    return arr

if __name__ == '__main__':
    swap()