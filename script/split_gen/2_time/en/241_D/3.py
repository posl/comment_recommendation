def bisect_left(a, x, lo=0, hi=None): # find leftmost value greater than or equal to x
    hi = hi if hi is not None else len(a) # hi defaults to len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < x: lo = mid+1
        else: hi = mid
    return lo
