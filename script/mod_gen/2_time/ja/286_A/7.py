def swap(arr, p, q, r, s):
    #print(arr)
    #print(p, q, r, s)
    #print(arr[p-1:q])
    #print(arr[r-1:s])
    tmp = arr[p-1:q]
    arr[p-1:q] = arr[r-1:s]
    arr[r-1:s] = tmp
    return arr

if __name__ == '__main__':
    swap()