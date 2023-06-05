def evenSum(n, a):
    a.sort()
    if a[0] == 0 and a[1] == 0:
        return 0
    elif a[0] == 0 and a[1] == 1:
        return -1
    elif a[0] == 0 and a[1] > 1:
        return a[1] - 1
    elif a[0] == 1:
        return -1
    else:
        return a[0] + a[1]
