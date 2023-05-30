def countGreater(arr, n, k):
    l = 0
    r = n - 1
    leftGreater = n
    while (l <= r):
        m = int(l + (r - l) / 2)
        if (arr[m] >= k):
            leftGreater = m
            r = m - 1
        else:
            l = m + 1
    return (n - leftGreater)
 
# Driver program
n,q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for i in range(q):
    k = int(input())
    print(countGreater(arr, n, k))
