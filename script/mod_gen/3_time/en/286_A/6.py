def swap(arr, p, q, r, s):
    b = arr.copy()
    for i in range(p-1, q):
        b[i] = arr[i+r-q]
    for i in range(r-1, s):
        b[i] = arr[i-q+p]
    return b

if __name__ == '__main__':
    swap()