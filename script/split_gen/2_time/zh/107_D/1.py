def median(a):
    b = sorted(a)
    m = len(b) // 2
    if len(b) % 2 == 0:
        return (b[m-1] + b[m]) // 2
    else:
        return b[m]
