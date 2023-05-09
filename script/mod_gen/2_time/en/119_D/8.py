def lower_bound(a, x):
    ok = -1
    ng = len(a)
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if a[mid] < x:
            ok = mid
        else:
            ng = mid
    return ng

if __name__ == '__main__':
    lower_bound()