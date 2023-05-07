def swap(arr, p, q, r, s):
    if p > q or r > s:
        return arr
    if s - r != q - p:
        return arr
    if p < 0 or q < 0 or r < 0 or s < 0:
        return arr
    if p >= len(arr) or q >= len(arr) or r >= len(arr) or s >= len(arr):
        return arr
    if p > r:
        return arr
    if q > s:
        return arr
    if p == r and q == s:
        return arr
    if p == r and q != s:
        arr[p], arr[q+1:s+1] = arr[q+1:s+1], arr[p]
        return arr
    if p != r and q == s:
        arr[p:r+1], arr[q] = arr[q], arr[p:r+1]
        return arr
    if p != r and q != s:
        arr[p:r+1], arr[q:s+1] = arr[q:s+1], arr[p:r+1]
        return arr

if __name__ == '__main__':
    swap()