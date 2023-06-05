def problems227_d(n,k,alist):
    alist.sort()
    print(alist)
    count = 0
    for i in range(0,n-k,k):
        count = count + 1
    print(count)
    return count
