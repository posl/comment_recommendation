def median(a):
    a = sorted(a)
    if len(a) % 2 == 0:
        return (a[len(a)//2] + a[len(a)//2-1]) / 2
    else:
        return a[len(a)//2]
