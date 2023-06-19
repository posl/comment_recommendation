def swap(arr, p, q, r, s):
    arr[p-1:q], arr[r-1:s] = arr[r-1:s], arr[p-1:q]
    return arr
n, p, q, r, s = map(int, input().split())
arr = list(map(int, input().split()))
print(*swap(arr, p, q, r, s))
