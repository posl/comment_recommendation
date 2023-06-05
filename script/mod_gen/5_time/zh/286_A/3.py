def swap(arr, p, q, r, s):
    arr1 = arr[p : q + 1]
    arr2 = arr[r : s + 1]
    arr[p : q + 1] = arr2
    arr[r : s + 1] = arr1
    return arr

if __name__ == '__main__':
    swap()