def find_median(a):
    a.sort()
    n = len(a)
    if n % 2 == 1:
        return a[n//2]
    else:
        return a[n//2-1]
