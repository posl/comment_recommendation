def find_median(a):
    a.sort()
    if len(a)%2 == 0:
        return a[len(a)//2-1]
    else:
        return a[len(a)//2]
