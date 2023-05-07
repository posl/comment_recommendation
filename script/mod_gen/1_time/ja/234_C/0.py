def binary_search(a, x):
    ok = 0
    ng = len(a)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if a[mid] >= x:
            ng = mid
        else:
            ok = mid
    return ok

if __name__ == '__main__':
    binary_search()