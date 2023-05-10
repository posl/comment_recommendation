def minimum_difference():
    #input
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    #sort
    a.sort()
    b.sort()
    #initialize
    min_diff = 10 ** 9 + 1
    #search
    i = 0
    j = 0
    while i < n and j < m:
        diff = abs(a[i] - b[j])
        if min_diff > diff:
            min_diff = diff
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    #output
    print(min_diff)
