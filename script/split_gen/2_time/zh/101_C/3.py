def solve(n,k,a):
    min = 100000000
    for i in range(n-k+1):
        if a[i] < min:
            min = a[i]
        if a[i+k-1] < min:
            min = a[i+k-1]
    return min
